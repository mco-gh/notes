Learn CSS Flexbox in 3 Minutes – Learning New Stuff – Medium

# Learn CSS Flexbox in 3 Minutes

![](../_resources/8e8cfa983a732cffb6fea3377ae7caf3.png)![1*baslR_nGORHYX4STOjhhpg.png](../_resources/db141d5d2a8f240acf5eba86e036be16.png)

In this post you’ll learn the **most important** concepts of the flexbox layout in CSS, which will make your life easier if you find yourself struggling with CSS layouts from time to time.

We’ll only focus on core principles, while leaving out stuff you **shouldn’t care about** until you’ve understood the basics.

### **1. The container and the item**

The two main components of a flexbox layout is the **container** (blue) and the **items** (red). In the example we’ll be looking at in this tutorial, both the **container** and **item** are *div’s. *Check out the [boilerplate code here](https://github.com/perborgen/FlexboxTutorial) if you’re interested.

#### Horizontal layout

To create a flex layout, simply give the **container** the following CSS property.

.container {
display: flex;
}
Which will result in this layout:

![](../_resources/25df4ccdd6e523231132e8d983f97152.png)![1*3zzvOetr1fjDrZKEEmo9dA.png](../_resources/8302eeef6eaed32baef48b35a330a690.png)

Notice that you don’t need to do anything with the **items** yet. They’ll be nicely positioned along the horizontal axis automatically.

#### Vertical layout

In the layout above, the **main axis **is the horizontal one, and the **cross axis** is the vertical one. The concept of **axes** are important to understand in order to use flex properly.

You can swap the two axes by adding *flex-direction*: *column.*
.container {
display: flex;
flex-direction: column;
}

![](../_resources/390a15b028d4912d64ce65b96e16265d.png)

Now the **main axis** is vertical and the **cross axis **horizontal, resulting in the **items **being stacked vertically.

### 2. Justify content and Align items

To make list horizontal again, we can switch the *flex-direction* from **column **to **row, **as this**  **flips the flex layout’s axes back again.

The reason the axes are important to understand is because the attributes *justify-content* and *align-items *control how the items are positioned along the **main axis **and **cross axis** respectively.

Let’s center all the items along the **main axis **by using **justify-content:**

.container {
display: flex;
flex-direction: row;
justify-content: center;
}

![](../_resources/59065fbc9cfc2d1c947912c4bfad2097.png)
And let’s adjust them along the **cross axis, **using *align-items.*
.container {
display: flex;
flex-direction: row;
justify-content: center;
align-items: center;
}

![](../_resources/e9617e47b04502cda91c0126deecf823.png)

Below are the other values you can set for *justify-content *and* align-items:.*

#### **justify-content:**

- •flex-start (**default**)
- •flex-end
- •center
- •space-between
- •space-around

#### **align-items:**

- •flex-start **(default)**
- •flex-end
- •center
- •baseline
- •stretch

I’d recommend you to play around with the *justify-content *and *align-items *properties in combination with the *flex-direction* being both column & row. That should give you a proper understanding of the concept.

### 3. The items

The last thing we’ll learn about is the **items** themselves, and how to add specific styles to each of them.

Let’s say we wanna adjust the position of the first item. We do this by giving it a CSS attribute of* align-self*, which accepts the exact same values as *align-items*:

.item1 {
align-self: flex-end;
}
Resulting in the following layout:

![](../_resources/9add54f3b97d28b577927d98365fba8d.png)
And that’s it!

There is of course a whole lot more to learn about flexbox, but the concepts above are the once I use the most often, and thus most important to understand properly.