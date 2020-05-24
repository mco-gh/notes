Build an app to generate photorealistic faces using TensorFlow and Streamlit

# Build an app to generate photorealistic faces using TensorFlow and Streamlit

## We’ll show you how to quickly build a Streamlit app to synthesize celebrity faces using GANs, Tensorflow, and st.cache.

[![2*p1XpZztbSsl7q45ooNneSQ.jpeg](../_resources/f4b96b152b6a66c74fd088123e85fff2.jpg)](https://towardsdatascience.com/@adrien.g.treuille?source=post_page-----dd2545828021----------------------)

[Adrien Treuille](https://towardsdatascience.com/@adrien.g.treuille?source=post_page-----dd2545828021----------------------)

[Apr 1](https://towardsdatascience.com/build-an-app-to-synthesize-photorealistic-faces-using-tensorflow-and-streamlit-dd2545828021?source=post_page-----dd2545828021----------------------) · 10 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='star-15px_svg__svgIcon-use js-evernote-checked' width='15' height='15' viewBox='0 0 15 15' style='margin-top:-2px' data-evernote-id='197'%3e%3cpath d='M7.44 2.32c.03-.1.09-.1.12 0l1.2 3.53a.29.29 0 0 0 .26.2h3.88c.11 0 .13.04.04.1L9.8 8.33a.27.27 0 0 0-.1.29l1.2 3.53c.03.1-.01.13-.1.07l-3.14-2.18a.3.3 0 0 0-.32 0L4.2 12.22c-.1.06-.14.03-.1-.07l1.2-3.53a.27.27 0 0 0-.1-.3L2.06 6.16c-.1-.06-.07-.12.03-.12h3.89a.29.29 0 0 0 .26-.19l1.2-3.52z' data-evernote-id='198' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='203'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='204' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/dd2545828021/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='212'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='213' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/dd2545828021/share/facebook?source=post_actions_header---------------------------)

![0*kqTo76YSl92YkYDV](../_resources/c97385143d064e8d42b0a024d5938e3f.png)
![0*kqTo76YSl92YkYDV](../_resources/23a6b74c4401b0ea7deccea95ea7ff5c.png)
[GAN-synthesized face]

Machine learning models are black boxes. Yes, you can run them on test sets and plot fancy performance curves, but it’s *still* often hard to answer basic questions about how they perform. A surprisingly powerful source of insight is simply to **play with your models**! Tweak inputs. Watch outputs. Let your coworkers and managers play with them too. This interactive approach is not only a powerful way to gain intuition, but also a great way to get people excited about your work.

Making interactive models is one of the use-cases that inspired [Streamlit](http://streamlit.io/), a Python framework that makes [writing apps as easy as writing Python scripts](https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace?source=friends_link&sk=f7774c54571148b33cde3ba6c6310086). This overview will walk you through creating a Streamlit app to play with one of the hairiest and black-box-iest models out there: a deep *Generative Adversarial Network* (GAN). In this case, we’ll visualize Nvidia’s [PG-GAN](https://research.nvidia.com/publication/2017-10_Progressive-Growing-of) [1] using TensorFlow to synthesize photorealistic human faces from thin air. Then, using Shaobo Guan’s amazing [TL-GAN](https://blog.insightdatascience.com/generating-custom-photo-realistic-faces-using-ai-d170b1b59255) model [2], we’ll create an [app that gives us](https://github.com/streamlit/demo-face-gan) the ability to tweak GAN-synthesized celebrity faces by attributes like age, smileyness, male likeness, and hair color. By the end of the tutorial, you’ll have a fully parametric model of humans! (Note we didn’t create the attributes. They came from the [CelebA dataset](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html) [3], and some of them can get a bit weird…)

# Getting started with Streamlit

If you haven’t installed Streamlit yet, you can do so by running:
pip install streamlit
streamlit hello

And if you’re a seasoned Streamlit-er, you’ll need to be on 0.57.1 or later, so make sure to upgrade!

pip install --upgrade streamlit

# Setting up your environment

Before we begin, use the commands below to check out the project’s GitHub repo and running the [Face GAN demo](https://github.com/streamlit/demo-face-gan) for yourself. This demo depends on Tensorflow 1, which does not support Python 3.7 or 3.8, so you’ll need Python 3.6. On Mac and Linux, we recommend using [pyenv](https://github.com/pyenv/pyenv) to install Python 3.6 alongside your current version, then setting up a new virtual environment using venv or virtualenv. On Windows, the [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/) allows you to [pick your Python version](https://docs.anaconda.com/anaconda/navigator/tutorials/use-multiple-python-versions/) with a point-and-click interface.

When you’re all set, open a terminal window and type:
git clone https://github.com/streamlit/demo-face-gan.git
cd demo-face-gan
pip install -r requirements.txt
streamlit run app.py

Give it a minute to finish downloading the trained GAN and then try playing with the sliders to explore the different faces the GAN can synthesize. Pretty cool, right?

![1*u-XAUMWozCKyaz1a_t_r-g.gif](../_resources/cda75336513a4117d252ca1c5a4179c6.jpg)
![1*u-XAUMWozCKyaz1a_t_r-g.gif](../_resources/3fd07538560900543bffb7a946e20d80.gif)

The full app code is a file that has ~190 lines of code, out of which only 13 are Streamlit calls. **That’s right, the entire UI above is drawn from just those 13 lines!**

Let’s take a look at how the app is structured:

|     |     |
| --- | --- |
| 1   | def  main(): |
| 2   |  st.title("Streamlit Face-GAN Demo") |
| 3   |     |
| 4   |  # Step 1. Download models and data files. |
| 5   |  for  filename  in  EXTERNAL_DEPENDENCIES.keys(): |
| 6   |  download_file(filename) |
| 7   |     |
| 8   |  # Step 2. Read in models from the data files. |
| 9   |  tl_gan_model, feature_names  =  load_tl_gan_model() |
| 10  |  session, pg_gan_model  =  load_pg_gan_model() |
| 11  |     |
| 12  |  # Step 3. Draw the sidebar UI. |
| 13  | ... |
| 14  |  features  = ... # Internally, this uses st.sidebar.slider(), etc. |
| 15  |     |
| 16  |  # Step 4. Synthesize the image. |
| 17  |  with  session.as_default(): |
| 18  |  image_out  =  generate_image(session, pg_gan_model, tl_gan_model, |
| 19  |  features, feature_names) |
| 20  |     |
| 21  |  # Step 5. Draw the synthesized image. |
| 22  |  st.image(image_out, use_column_width=True) |

 [view raw](https://gist.github.com/tc87/c6292bfa778fb5a2695325d47ce198b3/raw/9c158f249d5c2e37dd15f5b6a182b56ebd732d6f/face-gan-main.py)  [face-gan-main.py](https://gist.github.com/tc87/c6292bfa778fb5a2695325d47ce198b3#file-face-gan-main-py) hosted with ❤ by [GitHub](https://github.com/)

Now that you have a sense of how it is structured, let’s dive into each of the 5 steps above to see how they work.

# Step 1. Download models and data files

This step downloads the files we need: a pre-trained PG-GAN model and a TL-GAN model pre-fitted to it (we’ll dive into these a little bit later!).

The `download_file` utility function is a little smarter than a pure downloader:

- It checks if the file is already present in the local directory, so it only downloads it if needed. It also checks if the downloaded file’s size is what we expected it to be, so it’s able to fix interrupted downloads. This is a great pattern to follow!

|     |     |
| --- | --- |
| 1   | # If the file exists and has the expected size, return. |
| 2   | if  os.path.exists(file_path): |
| 3   |  if  "size"  not  in  EXTERNAL_DEPENDENCIES[file_path]: |
| 4   |  return |
| 5   |  elif  os.path.getsize(file_path) ==  EXTERNAL_DEPENDENCIES[file_path]["size"]: |
| 6   |  return |

 [view raw](https://gist.github.com/tc87/5ef9709e29cfd4311bf5cf19d4b1397f/raw/b6523847de9965795c4cd14a92128e7ca6421aa8/face-gan-download_file.py)  [face-gan-download_file.py](https://gist.github.com/tc87/5ef9709e29cfd4311bf5cf19d4b1397f#file-face-gan-download_file-py) hosted with ❤ by [GitHub](https://github.com/)

- It uses `st.progress()` and `st.warning()` to show a nice UI to the user while the file downloads. Then it calls `.empty()` on those UI elements to hide them when done.

|     |     |
| --- | --- |
| 1   | # Draw UI elements. |
| 2   | weights_warning  =  st.warning("Downloading %s..."  %  file_path) |
| 3   | progress_bar  =  st.progress(0) |
| 4   |     |
| 5   | with  open(file_path, "wb") as  output_file: |
| 6   |  with  urllib.request.urlopen(...) as  response: |
| 7   |     |
| 8   | ... |
| 9   |     |
| 10  |  while  True: |
| 11  |     |
| 12  | ... # Save downloaded bytes to file here. |
| 13  |     |
| 14  |  # Update UI elements. |
| 15  |  weights_warning.warning( |
| 16  |  "Downloading %s... (%6.2f/%6.2f MB)"  % |
| 17  | (file_path, downloaded_size)) |
| 18  |  progress_bar.progress(downloaded_ratio) |
| 19  |     |
| 20  | ... |
| 21  |     |
| 22  | # Clear UI elements when done. |
| 23  | weights_warning.empty() |
| 24  | progress_bar.empty() |

 [view raw](https://gist.github.com/tc87/2dd80d668f36e102647ff04305862384/raw/de6f6b5cf0a600456ffbfdc8510e037465699e22/face-gan-UI.py)  [face-gan-UI.py](https://gist.github.com/tc87/2dd80d668f36e102647ff04305862384#file-face-gan-ui-py) hosted with ❤ by [GitHub](https://github.com/)

# Step 2. Load the models into memory

The next step is to load these models into memory. Here is the code for loading the PG-GAN model:

|     |     |
| --- | --- |
| 1   | @st.cache(allow_output_mutation=True, hash_funcs=TL_GAN_HASH_FUNCS) |
| 2   | def  load_pg_gan_model(): |
| 3   |  """ |
| 4   | Create the tensorflow session. |
| 5   | """ |
| 6   |  config  =  tf.ConfigProto(allow_soft_placement=True) |
| 7   |  session  =  tf.Session(config=config) |
| 8   |     |
| 9   |  with  session.as_default(): |
| 10  |  with  open(MODEL_FILE_GPU  if  USE_GPU  else  MODEL_FILE_CPU, 'rb') as  f: |
| 11  |  G  =  pickle.load(f) |
| 12  |  return  session, G |

 [view raw](https://gist.github.com/tc87/585976da558b9ca87724f9136e335565/raw/43cb239e71b59e35978295a48e921a0b1f45f0f0/face-gan-load-pg.py)  [face-gan-load-pg.py](https://gist.github.com/tc87/585976da558b9ca87724f9136e335565#file-face-gan-load-pg-py) hosted with ❤ by [GitHub](https://github.com/)

Notice the `@st.cache` decorator at the start of `load_pg_gan_model()`. Normally in Python, you could just run `load_pg_gan_model()` and reuse that variable over and over. Streamlit’s [execution model](https://docs.streamlit.io/main_concepts.html?highlight=execution%20model#data-flow) is unique, however, in that every time a user interacts with a UI widget your script executes again *in*  *its entirety, *from top to bottom. By adding `@st.cache` to the costly model-loading functions, we are telling Streamlit to only run those functions the first time the script executes — and just reuse the cache output for every execution after that. That is one of Streamlit’s most fundamental features, as it lets you run scripts efficiently by caching the results of function calls. This way, the large fitted GAN models will be loaded into memory exactly once; and by the same token, our TensorFlow session will be created exactly once, as well. (See our [launch article](https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace?source=friends_link&sk=f7774c54571148b33cde3ba6c6310086) for a refresher on Streamlit’s execution model.)

![0*RLK-hVUVjSVhr62f](../_resources/109cf249ee607285081d5956bb8cf761.png)
![0*RLK-hVUVjSVhr62f](../_resources/097dafff76c03f733f695cbe3bbc4aa2.png)
[Figure 1. How caching works in Streamlit’s execution model]

There’s one wrinkle, though: the TensorFlow session object can mutate internally as we use it to run different computations. Ordinarily, [we don’t want cached objects to mutate](https://docs.streamlit.io/caching.html#example-6-mutating-cached-values), as that can lead to unexpected results. So when Streamlit detects such mutations, it issues a warning to the user. However, in this case we happen to know that it’s OK if the TensorFlow session object mutates, so [we bypass the warning](https://docs.streamlit.io/troubleshooting/caching_issues.html#how-to-fix-the-cached-object-mutated-warning) by setting `allow_output_mutation=True`.

# Step 3. Draw the sidebar UI

If this is the first time you’re seeing Streamlit’s API for drawing widgets, here’s the 30-second crash course:

- You add widgets by calling API methods like `st.slider()` and `st.checkbox()`.
- The return value of those methods is the value shown in the UI. For example, when the user moves a slider to position 42, your script will be re-executed and in that execution the return value of that `st.slider()` will be 42.
- You can put anything in a sidebar by prepending it with `st.sidebar`. For example, `st.sidebar.checkbox()`.

So to add a slider in the sidebar, for example — a slider to allow the user to tune the `brown_hair` parameter, you would just add:

|     |     |
| --- | --- |
| 1   | brown_hair  =  st.sidebar.slider("Brown Hair", 0, 100, 50, step=5) |
| 2   | # Translation: Draw a slider from 0 to 100 with steps of size 5. |
| 3   | # Then set the default value to 50. |

 [view raw](https://gist.github.com/tc87/239851c78e49adf35c5282403f41465d/raw/bfe370a6071967580a9b880274a6885a23b5eb24/face-gan-sidebar.py)  [face-gan-sidebar.py](https://gist.github.com/tc87/239851c78e49adf35c5282403f41465d#file-face-gan-sidebar-py) hosted with ❤ by [GitHub](https://github.com/)

In our app we want to get a little fancy to show off just how easy it is to make the UI itself modifiable in Streamlit! We want to allows users to first use a multiselect widget to pick a set of features they want to control in the generated image, which means our UI needs to be drawn programmatically:

![0*BwanS6qqSNmjZr66](../_resources/77fef987c57b1cbc4fe1e40b340f9732.png)
![0*BwanS6qqSNmjZr66](../_resources/66729c962c1e72d261db209e1730eed1.png)
With Streamlit, the code for that is actually quite simple:

|     |     |
| --- | --- |
| 1   | st.sidebar.title('Features') |
| 2   |     |
| 3   | ... |
| 4   |     |
| 5   | # If the user doesn't want to select which features to control, these will be used. |
| 6   | default_control_features  = ['Young','Smiling','Male'] |
| 7   |     |
| 8   | if  st.sidebar.checkbox('Show advanced options'): |
| 9   |  # Randomly initialize feature values. |
| 10  |  features  =  get_random_features(feature_names, seed) |
| 11  |     |
| 12  |  # Let the user pick which features to control with sliders. |
| 13  |  control_features  =  st.sidebar.multiselect( |
| 14  |  'Control which features?', |
| 15  |  sorted(features), default_control_features) |
| 16  |     |
| 17  | else: |
| 18  |  features  =  get_random_features(feature_names, seed) |
| 19  |     |
| 20  |  # Don't let the user pick feature values to control. |
| 21  |  control_features  =  default_control_features |
| 22  |     |
| 23  | # Insert user-controlled values from sliders into the feature vector. |
| 24  | for  feature  in  control_features: |
| 25  |  features[feature] =  st.sidebar.slider(feature, 0, 100, 50, 5) |

 [view raw](https://gist.github.com/tc87/b7c9d5870afed0d7300c6be5f20badfd/raw/2559c538488791bf7928a3a9eb874a56223007a3/face-gan-main2-alt.py)  [face-gan-main2-alt.py](https://gist.github.com/tc87/b7c9d5870afed0d7300c6be5f20badfd#file-face-gan-main2-alt-py) hosted with ❤ by [GitHub](https://github.com/)

# Step 4. Synthesize the image

Now that we have a set of features telling us what kind of face to synthesize, we need to do the heavy lifting of synthesizing the face. The way we’ll do that is by passing the features into the TL-GAN to generate a vector in the PG-GAN’s latent space, then feed that vector to PG-GAN. If that sentence made no sense to you, let’s take a detour and talk about how our two neural nets work.

# **A detour into GANs**

To understand how the above app generates faces from slider values, you first have to understand something about how PG-GAN and TL-GAN work — but don’t worry, **you can skip this section and still understand how the app works at a higher level!**

PG-GAN, like any GAN, is fundamentally* a pair* of neural networks, one generative and one discriminative, which are trained against each other, forever locked in mortal combat. The generative network is in charge of synthesizing images it believes look like faces, and the discriminative network is in charge of deciding whether or not the images are indeed faces. The two networks are iteratively trained against each other’s output, so each one does its best to learn to fool the other network. The end result is the final generative network is able to synthesize realistic-looking faces even though at the start of training all it could synthesize was random noise. Its really quite amazing! In this case, the face-generating GAN we use was trained on celebrity faces by Karras *et al* using their [Progressive Growing of GANs](https://github.com/tkarras/progressive_growing_of_gans) algorithm (PG-GAN), which trains GANs using progressively higher-resolution images. [1]

The input to PG-GAN is a high-dimensional vector belonging to its so-called *latent-space*. The latent-space is basically the space of all possible faces the network can generate, so each random vector in that space corresponds to a unique face (or at least it should! Sometimes you get weird results…) The way you typically use a GAN is to give it a random vector and then check out what face gets synthesized (Figure 2.a).

![0*5LDbOi-hV71ZcNhi](../_resources/a3d473540c7ee6a22675bc32bc7df39f.png)
![0*5LDbOi-hV71ZcNhi](../_resources/9ce3b6f2460bd928eb5f80804a8f4a86.png)
[Figure 2.a]

However, that sounds a bit dull and we’d rather have some more control over the output. We’d like to tell PG-GAN “generate an image of a man with a beard”, or “generate an image of a brown-haired woman”. That’s where the TL-GAN comes in.

The TL-GAN is yet another neural network, this one trained by entering random vectors into PG-GAN, taking the generated faces, and running them through classifiers for attributes like “is young-looking”, “is bearded”, “is brown-haired”, etc. In the training phase, TL-GAN labels thousands of faces from PG-GAN with those classifiers and identifies directions in the latent space that correspond to changes in the labels we care about. As a result, the TL-GAN learns how to map those classes (i.e. “young-looking”, “bearded”, “brown-haired”) into the appropriate random-looking vector that should be input into PG-GAN to generate a face with those characteristics (Figure 2.b).

![0*0yIP_XPlxdddzS4B](../_resources/fe6502d2515d43f4aa41d9b57d387237.png)
![0*0yIP_XPlxdddzS4B](../_resources/ac35e9859e51d940abb337e374c38d34.png)
[Figure 2.b]

Going back to our app, at this point we’ve already downloaded the pre-trained GAN models and loaded them into memory, and we’ve also grabbed a feature vector from the UI. So now we just have to feed those features into TL-GAN and then PG-GAN to get an image out:

|     |     |
| --- | --- |
| 1   | @st.cache(show_spinner=False, hash_funcs={tf.Session: id}) |
| 2   | def  generate_image(session, pg_gan_model, tl_gan_model, features, feature_names): |
| 3   |     |
| 4   |  # Create rescaled feature vector. |
| 5   |  feature_values  =  np.array([features[name] for  name  in  feature_names]) |
| 6   |  feature_values  = (feature_values  -  50) /  250 |
| 7   |     |
| 8   |  # Multiply by Shaobo's matrix to get the latent variables. |
| 9   |  latents  =  np.dot(tl_gan_model, feature_values) |
| 10  |  latents  =  latents.reshape(1, -1) |
| 11  |  dummies  =  np.zeros([1] +  pg_gan_model.input_shapes[1][1:]) |
| 12  |     |
| 13  |  # Feed the latent vector to the GAN in TensorFlow. |
| 14  |  with  session.as_default(): |
| 15  |  images  =  pg_gan_model.run(latents, dummies) |
| 16  |     |
| 17  |  # Rescale and reorient the GAN's output to make an image. |
| 18  |  images  =  np.clip(np.rint((images  +  1.0) /  2.0  *  255.0), |
| 19  |  0.0, 255.0).astype(np.uint8) # [-1,1] => [0,255] |
| 20  |     |
| 21  |  if  USE_GPU: |
| 22  |  images  =  images.transpose(0, 2, 3, 1) # NCHW => NHWC |
| 23  |     |
| 24  |  return  images[0] |

 [view raw](https://gist.github.com/tc87/451b765a7d23c7b210b9135a41dbf910/raw/0366ddc94f111d16458d7f4dd20afbaa69d13be3/face-gan-gen-def.py)  [face-gan-gen-def.py](https://gist.github.com/tc87/451b765a7d23c7b210b9135a41dbf910#file-face-gan-gen-def-py) hosted with ❤ by [GitHub](https://github.com/)

# Optimize performance

The `generate_image()` function above can take some time to execute, especially when running on a CPU. To improve our app’s performance it would be great if we could cache the output of that function, so we don’t have to re-synthesize faces we’ve already seen as we move the slider back and forth.

Well, as you may have noticed in the snippet above already, the solution here is to once again use the `@st.cache` decorator.

But notice the two arguments we passed to `@st.cache` in this case: `show_spinner=False` and `hash_funcs={tf.Session: id}`. What are those there for?

The first one is easy to explain: by default, `@st.cache` shows a status box in the UI letting you know that a slow-running function is currently executing. We call that a “spinner”. However, in this case, we’d like to avoid showing it, so the UI doesn’t jump around unexpectedly. So we set `show_spinner` to False.

The next one solves a more involved problem: the TensorFlow session object, which is passed as an argument to `generate_image()`, is usually mutated by TensorFlow’s internals in between runs of this cached function. This means the input arguments to `generate_image()` will always be different and we’ll never actually get a cache hit. In other words, the `@st.cache` decorator won’t actually do anything! How can we solve this?

# Hash_funcs to the rescue

The hash_funcs option allows us to specify custom hash functions that tell `@st.cache` how it should interpret different objects when checking whether this is a cache hit or a cache miss. In this case, we’re going to use that option to tell Streamlit to hash a TensorFlow session by calling Python’s `id()` function rather than by examining its contents:

|     |     |
| --- | --- |
| 1   | @st.cache(..., hash_funcs={tf.Session: id}) |
| 2   | def  generate_image(session, ...): |
| 3   | ... |

 [view raw](https://gist.github.com/tc87/0120fdc6aa703449a05a3019f35bf7a2/raw/805cd391bd98fc0934244934f05d9e6f136b1dbd/face-gan-hash-funcs.py)  [face-gan-hash-funcs.py](https://gist.github.com/tc87/0120fdc6aa703449a05a3019f35bf7a2#file-face-gan-hash-funcs-py) hosted with ❤ by [GitHub](https://github.com/)

This works for us because the session object in our case is actually a singleton across all executions of the underlying code since it comes from the @st.cache’d `load_pg_gan_model()` function.

For more information about `hash_funcs`, check out our documentation about [advanced caching techniques](https://docs.streamlit.io/api.html?highlight=cache#streamlit.cache).

# Step 5. Draw the synthesized image

Now that we have the output image, drawing it is a piece of cake! Just call Streamlit’s `st.image` function:

st.image(image_out, use_column_width=True)
And we’re done!

# Wrapping up

So there you have it: interactive face synthesis with TensorFlow in a 190-line Streamlit app and only 13 Streamlit function calls! Have fun exploring the space of faces these two GANs can draw, and many thanks to [Nvidia](https://github.com/tkarras/progressive_growing_of_gans) and [Shaobo Guan](https://github.com/SummitKwan/transparent_latent_gan) for letting us build off their super cool demos. We hope that you have as much fun building apps and playing with models as we do.

For more Streamlit app examples, you can check out our gallery at[https://www.streamlit.io/gallery.