Weighted Random Draws in Go

# Weighted Random Draws in Go

 *  ** Posted on January 24, 2019  | ** 7 minutes  | ** 1377 words  | ** Milos Gajdos *

When working on my last [project](https://github.com/milosgajdos83/go-filter) I needed to find a way to draw a random number from a list based on some weight assigned to it i.e. given a list of numbers each of which has a weight assigned to it, I had to find a way to draw a number from the list based on the weight. The numbers which have higher weight assigned to them should be more likely to be drawn than the numbers with lower weights.

After making a few, rather unsuccessful, attempts at solving the problem I decided to take it on the internet to answer the endless stream of questions that this problem generated in my head. Few minutes of research led me to discovering [Fitness proportionate selection](https://en.wikipedia.org/wiki/Fitness_proportionate_selection) problem a.k.a. *roulette wheel selection* problem. Wikipedia provides some pseudocode examples that got me on the right track to solve my problem, but I haven’t stopped there. I continued to search the web and eventually landed on the brilliant [blog post](http://www.keithschwarz.com/darts-dice-coins/) by [Keith Schwarz](http://www.keithschwarz.com/me/) which explains different variants of random draws and solutions to how to implement them efficiently.

As I learnt there are different ways of solving my problem. I decided to settle on the solution described in *Generalizing Biased Coins: Simulating Loaded Dice* paragraph as it seemed to provide reasonable performance and, judging by the example pseudocode, it seemed easy to implement using [Go](https://golang.org/) standard library and the wonderful [gonum](https://www.gonum.org/) library for numerical computing.

# Roulette wheel selection

As usually, once you understand the problem well enough, the actual implementation of the solution is usually not that hard. But let’s first discuss the pseudocode listed on Keith Schwartz’s excellent post. The algorithm to solving this problem has two parts:

Initialization:
Allocate an array A of size n
1. Set A[0]=p0.
2. For each probability i from 1 to n−1:
3. Set A[i]=A[i−1]+pi
Generation:
1. Generate a uniformly-random value x in the range [0,1)

2. Using a binary search, find the index i of the smallest element in A larger than x.

3. Return i.

Let’s now discuss how to go about implementing this algorithm in `Go` programming language.

## Initialization

The `Initialization` part is pretty simple. We have a slice of numerical values each of which represents a weight assigned to particular value (index of the slice). We then calculate *cumulative sum* slice from the weights. The resulting can then be considered [Cumulative distribution function](https://en.wikipedia.org/wiki/Cumulative_distribution_function) (CDF) of a random discrete variable:

	weights := []float64{1.0, 2.0, 4.0, 8.0, 10.0, 7.0}
	cdf := make([]float64, len(p))
	floats.CumSum(cdf, weights)

The `CumSum` function above comes from the `floats` package of the [gonum](https://godoc.org/gonum.org/v1/gonum/floats#CumSum) library. The `floats` package provides a whole suite of functions for working with slices of `float64`. The `cdf` slice in the code sample above now contains a list of `float`s **sorted** in ascending order. We will take advantage of this property in the generation part of the algorithm.

## Generation

The `Generation` part looks a bit more involved, but implementing it turned out to be a breeze. Once again, kudos to `Go` standard library and `gonum`. See the code below for the concrete implementation:

	// number of random draws
	n := 100
	indices := make([]int, n)
	// loop through indices and draw random values
	for i := range indices {
	        // multiply the sample with the largest CDF value; easier than normalizing to [0,1)
	        val = distuv.UnitUniform.Rand() * cdf[len(cdf)-1]
	        // Search returns the smallest index i such that cdf[i] > val
	        indices[i] = sort.Search(len(cdf), func(i int) bool { return cdf[i] > val })
	}

In this particular example I decided to do 100 random draws. `indices` slice will contain indices into `weights` slice pointing to the item with particular weight i.e. if the result returned by the algorithm is `3` we know that a value whose weight is `8.0` has just been drawn.

Now to the more interesting part. We start by drawing a random value in the range `[0, 1)` from continuous [Uniform distribution](https://en.wikipedia.org/wiki/Uniform_distribution_%28continuous%29) using the `distuv.UnitUniform.Rand()` function from the `stat/distuv` gonum package and multiply it with the last number of the previously calculated cumulative sum slice. This is the highest value in the slice. This multiplication gives us an (random) index into the cdf slice.

**Note:** We could also normalise the weights to values from `[0,1)` range, which would make multiplication with the last vaue of `cdf` unnecessary. In that case the weights slice would look like this (notice the sum of all weights add to `1`):

`weights := float64{0.03125, 0.0625, 0.125, 0.25, 0.3125, 0.21875}`

We now need to find the smallest index in this range which is larger than `val`. Since we know that the `cdf` is sorted in ascending order by definition, we can use the wonderful `sort.Search` function from the wonderful `Go` standard library. According to documentation [sort.Search](https://golang.org/pkg/sort/#Search)  *uses binary search to find and return the smallest index i in [0, n) at which f(i) is true…*. This fits our requirements perfectly. We store the result in `indices` slice and continue in the loop until we are done.

That’s it! You can find the full implementation in the `rand` package of my [go-filter](https://github.com/milosgajdos83/go-filter) library. Since the full implentation of the function is pretty small I am copy-pasting it here:

	// RouletteDrawN draws n numbers randomly from a probability mass function (PMF) defined by weights in p.
	// RouletteDrawN implements the Roulette Wheel Draw a.k.a. Fitness Proportionate Selection:
	// - https://en.wikipedia.org/wiki/Fitness_proportionate_selection
	// - http://www.keithschwarz.com/darts-dice-coins/
	// It returns a slice of n indices into the vector p.
	// It fails with error if p is empty or nil.
	func RouletteDrawN(p []float64, n int) ([]int, error) {
	        if p == nil || len(p) == 0 {
	                return nil, fmt.Errorf("Invalid probability weights: %v", p)
	        }
	        // Initialization: create the discrete CDF
	        // We know that cdf is sorted in ascending order
	        cdf := make([]float64, len(p))
	        floats.CumSum(cdf, p)
	        // Generation:
	        // 1. Generate a uniformly-random value x in the range [0,1)
	        // 2. Using a binary search, find the index of the smallest element in cdf larger than x
	        var val float64
	        indices := make([]int, n)
	        for i := range indices {
	                // multiply the sample with the largest CDF value; easier than normalizing to [0,1)
	                val = distuv.UnitUniform.Rand() * cdf[len(cdf)-1]
	                // Search returns the smallest index i such that cdf[i] > val
	                indices[i] = sort.Search(len(cdf), func(i int) bool { return cdf[i] > val })
	        }

	        return indices, nil
	}

# Example

Now if you would like to test it using a simple program here’s a simple one which will hopefully convince you the implementation works correctly:

	package main

	import (
		"fmt"
		"log"

		"github.com/milosgajdos83/go-filter/rand"
	)

	type Fruit struct {
		Name   string
		Weight float64
		Draws  int
	}

	func main() {
		items := map[int]*Fruit{
			0: &Fruit{Name: "Banana", Weight: 1},
			1: &Fruit{Name: "Lemon", Weight: 2},
			2: &Fruit{Name: "Apple", Weight: 4},
			3: &Fruit{Name: "Mellon", Weight: 8},
			4: &Fruit{Name: "Orange", Weight: 10},
			5: &Fruit{Name: "Pineapple", Weight: 7},
		}

		var p []float64
		for i, _ := range []int{0, 1, 2, 3, 4, 5} {
			p = append(p, items[i].Weight)
		}

		draws, err := rand.RouletteDrawN(p, 10000)
		if err != nil {
			log.Fatalf("Failed to generate Roulette samples: %v", err)
		}

		for _, val := range draws {
			items[val].Draws++
		}

		for k, _ := range items {
			fmt.Printf("Weight: %.2f, Draws: %d\n", items[k].Weight, items[k].Draws)
		}
	}

When I ran this I got the following results. Note your absolute `Draws` counts might differ, but the rankings **when ordered by draw counts** will be the same:

Weight: 10.00, Draws: 3062
Weight: 7.00, Draws: 2165
Weight: 1.00, Draws: 329
Weight: 2.00, Draws: 624
Weight: 4.00, Draws: 1279
Weight: 8.00, Draws: 2541

You can see the item with the highest weight (`10.0`) was indeed drawn the most frequently (`3062`), followed by the item with the second highest weight and so on.

# Conclusion

This blog post introduced one of many ways to generate a weighted random value using `Go` programming language. It highlighted the every so wonderful `Go` standard library, in particular its `sort` package, as well as one of my favourite `Go` libraries for scientific comupting, [gonum](https://www.gonum.org/).

Solving the problem of weighted random draw helped me implement one of the important pieces of [bootstrap particle filter](https://github.com/milosgajdos83/go-filter/tree/master/particle/bf) which is part of the [go-filter](https://github.com/milosgajdos83/go-filter) library I made last month. If you find this post useful let me know in the comments. Until next time!

Tags:   [#go](https://cybernetist.com/tags/go/)  [#golang](https://cybernetist.com/tags/golang/)  [#random](https://cybernetist.com/tags/random/)  [#simulation](https://cybernetist.com/tags/simulation/)

* * *

- [**](https://twitter.com/share?url=https%3a%2f%2fcybernetist.com%2f2019%2f01%2f24%2frandom-weighted-draws-in-go%2f&text=Weighted%20Random%20Draws%20in%20Go&via=milosgajdos)

- [**](https://plus.google.com/share?url=https%3a%2f%2fcybernetist.com%2f2019%2f01%2f24%2frandom-weighted-draws-in-go%2f)

- [**](https://www.facebook.com/sharer/sharer.php?u=https%3a%2f%2fcybernetist.com%2f2019%2f01%2f24%2frandom-weighted-draws-in-go%2f)

- [**](https://reddit.com/submit?url=https%3a%2f%2fcybernetist.com%2f2019%2f01%2f24%2frandom-weighted-draws-in-go%2f&title=Weighted%20Random%20Draws%20in%20Go)

- [**](https://www.linkedin.com/shareArticle?url=https%3a%2f%2fcybernetist.com%2f2019%2f01%2f24%2frandom-weighted-draws-in-go%2f&title=Weighted%20Random%20Draws%20in%20Go)

- [**](https://www.stumbleupon.com/submit?url=https%3a%2f%2fcybernetist.com%2f2019%2f01%2f24%2frandom-weighted-draws-in-go%2f&title=Weighted%20Random%20Draws%20in%20Go)

- [**](https://www.pinterest.com/pin/create/button/?url=https%3a%2f%2fcybernetist.com%2f2019%2f01%2f24%2frandom-weighted-draws-in-go%2f&description=Weighted%20Random%20Draws%20in%20Go)

#### See also

- [Tenus Golang Powered Linux Networking](https://cybernetist.com/2014/07/30/tenus-golang-powered-linux-networking/)

- [← Previous Post](https://cybernetist.com/2019/01/13/apollo-kalman-filter-and-go-filter/)

- [  **  **](https://github.com/milosgajdos83)

- [  **  **](https://twitter.com/milosgajdos)

- [  **  **](https://reddit.com/u/milosgajdos)

- [  **  **](https://linkedin.com/in/milosgajdos)

- [  **  **](https://cybernetist.com/index.xml)

 [Milos Gajdos](https://cybernetist.com/)  • © 2019  •  [Cybernetist](https://cybernetist.com/)

 [Hugo v0.53](https://gohugo.io/) powered  •  Theme by [Beautiful Jekyll](http://deanattali.com/beautiful-jekyll/) adapted to [Beautiful Hugo](https://github.com/halogenica/beautifulhugo)