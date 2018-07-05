# TinderAutomation

![Alt text](/img/tinder.png?raw=true "Optional Title")

## 1. Introduction

The other day, while I sat on the toilet to take a *poop*, I whipped out my phone, opened up the king of all toilet apps: Tinder. I clicked open the application and started the mindless swiping. *Left* *Right* *Left* *Right* *Left*.

Now that we have dating apps, everyone suddenly has access to exponentially more people to date compared to the pre-app era. The Bay Area tends to lean more men than women. The Bay Area also attracts uber-successful, smart men from all around the world. As a big-foreheaded, 5 foot 9 asian man who doesn't take many pictures, there's fierce competition within the San Francisco dating sphere.

From talking to female friends using dating apps, females in San Francisco can get a match almost every other swipe. Assuming females get 20 matches in an hour, they do not have the time to go out with every man that messages them. Obviously, they'll pick the man they like most based off their profile + initial message.

I'm an above-average looking guy. However, in a sea of asian men, based purely on looks, my face wouldn't pop out the page. In a stock exchange, we have buyers and sellers. The top investors earn a profit through informational advantages. At the poker table, you become profitable if you have a skill advantage over the other people on your table. If we think of dating as a "competitive marketplace", how do you give yourself the edge over the competition? A competitive advantage could be: amazing looks, career success, social-charm, adventurous, proximity, great social circle etc.

On dating apps, men & women who have a competitive advantage in photos & texting skills will reap the highest ROI from the app. As a result, I've broken down the reward system from dating apps down to a formula, assuming we normalize message quality from a 0 to 1 scale:

<p align="center"><img src ="/img/formula.gif" /></p>

The better photos/good looking you are you have, the less you need to write a quality message. If you have bad photos, it doesn't matter how good your message is, nobody will respond. If you have great photos, a witty message will significantly boost your ROI. If you don't do any swiping, you'll have zero ROI.

While I don't have the BEST pictures, my main bottleneck is that I just don't have a high-enough swipe volume. I just think that the mindless swiping is a waste of my time and prefer to meet people in person. However, the problem with this, is that this strategy severely limits the range of people that I could date. To solve this swipe volume problem, I decided to build an AI that automates tinder called: THE DATE-A MINER.

The DATE-A MINER is an artificial intelligence that learns the dating profiles I like. Once it finished learning what I like, the DATE-A MINER will automatically swipe left or right on each profile on my Tinder application. As a result, this will significantly increase swipe volume, therefore, increasing my projected Tinder ROI. Once I attain a match, the AI will automatically send a message to the matchee.

While this doesn't give me a competitive advantage in photos, this does give me an advantage in swipe volume & initial message. Let's dive into my methodology:

## 2. Data Collection 

To build the DATE-A MINER, I needed to feed her A LOT of images. As a result, I accessed the Tinder API using pynder. What this API allows me to do, is use Tinder through my terminal interface rather than the app:

<p align="center"><img src ="/img/sample_bot.png" /></p>

I wrote a script where I could swipe through each profile, and save each image to a "likes" folder or a "dislikes" folder. I spent hours and hours swiping and collected about 10,000 images.

One problem I noticed, was I swiped left for about 80% of the profiles. As a result, I had about 8000 in dislikes and 2000 in the likes folder. This is a severely imbalanced dataset. Because I have such few images for the likes folder, the date-ta miner won't be well-trained to know what I like. It'll only know what I dislike.

To fix this problem, I found images on google of people I found attractive. Then I scraped these images and used them within my dataset.

## 3. Data Pre-Processing

Now that I have the images, there are a number of problems. There is a wide range of images on Tinder. Some profiles have images with multiple friends. Some images are zoomed out. Some images are low quality. It would difficult to extract information from such a high variation of images.

To solve this problem, I used a [Haars Cascade Classifier Algorithm](https://docs.opencv.org/3.4.1/d7/d8b/tutorial_py_face_detection.html) to extract the faces from images and then saved it.

The Algorithm failed to detect the faces for about 70% of the data. As a result, my dataset was sliced into a dataset of 3,000 images. 

## 4. Modeling

To model this data, I used a Convolutional Neural Network. Because my classification problem was extremely detailed & subjective, I needed an algorithm that could extract a large enough amount of features to detect a difference between the profiles I liked and disliked. A cNN was also built for image classification problems.

To model this data, I used two approaches:

**3-Layer Model**: I didn't expect the three layer model to perform very well. Whenever I build any model, my goal is to get a dumb model working first. This was my dumb model. I used a very basic architecture:

```Python
model = Sequential()
model.add(Convolution2D(32, 3, 3, activation='relu', input_shape=(img_size, img_size, 3)))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Convolution2D(32, 3, 3, activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Convolution2D(64, 3, 3, activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
          
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(2, activation='softmax'))

adam = optimizers.SGD(lr=1e-4, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer= adam,
              metrics=['accuracy'])

```
The resulting accuracy was about 67%. 


**Transfer Learning using VGG19**: The problem with the 3-Layer model, is that I'm training the cNN on a SUPER small dataset: 3000 images. The best performing cNN's train on millions of images. 

As a result, I used a technique called "Transfer Learning." Transfer learning, is basically taking a model someone else built and using it on your own data. This is usually the way to go when you have an extremely small dataset. 

**Accuracy**:73% accuracy

**Precision** 59%

**Recall:** 44.61%

Accuracy is just predicting whether I liked or disliked the image correctly.

Precision, tells us "out of all the profiles that my algorithm predicted were true, how many did I actually like?" A low precision score would mean my algorithm wouldn't be useful since most of the matches I get are profiles I don't like.

Recall, tells us "out of all the profiles that I actually like, how many did the algorithm predict correctly?" If this score is low, it means the algorithm is being overly picky.

You can see here the algorithm predicting on Scarlet Johansson:

![Alt text](/img/scarlet_v2.png?raw=true "Optional Title")

## 5. Running the Bot

Now that I have the algorithm built, I needed to connect it to the bot. Builting the bot wasn't too difficult. Here, you can see the bot in action: 

![Alt text](/img/baetamining_bot.gif?raw=true "Optional Title")

I intentionally added a 3 to 15 second delay on each swipe so Tinder wouldn't find out that it was a bot running on my profile. Unfortunately, I did not have time to add a GUI to this program. 

## 6. Future Work
I gave myself only a month of part-time work to complete this project. In reality, there's an infinite number of additional things I could do:

**Body extract tool:** Use an algorithm to detect body size and images and use these images as training data. This would add another feature and create a stronger model.

**Natural Language Processing on Profile text/interest**: I could extract the profile description and facebook interests and incorporate this into a scoring metric to develop more accurate swipes. 

**Create a "total profile score"**: Rather than make a swipe decision off the first valid picture, I could have the algorithm look at every picture and compile the cumulative swipe decisions into one scoring metric to decide if she should swipe right or left. 

**More Data**: I only trained on 3,000 images. If I could train on 150,000 Tinder images, I'm confident I'd have an 80-90% performing algorithm. In addition, I could also improve the facial extraction program, so I'm not losing 70% of my data. 

**Adapt to Hinge, Coffee Meets Bagel, Bumble:** To widen my quantity, adapt the algorithm to hit multiple channels:

**A/B Testing**: Having a framework to AB test different messages, profile pictures and have analytics supporting these different decisions. 

**Google's Inception, VGG16**: These are different pre-trained cNN's. I wanted to try these but I ran out of time.

**Add GUI/Turn into a user-friendly app**: This would allow non-technical people to use this.

## 7. Installation 

To install everything, follow these instructions:

You must have the correct packages installed. To install the packages run the following command on the commandline:

```pip install -r requirements.txt```

Once you have the requirements installed, you'll need to get your FB authentication token & ID and store it in the `auth.json` file. I have a script in here to extract the token called helpers.py so run that script. 

If you're running into issues. Read [this](https://github.com/charliewolf/pynder/issues/136) to get your ID. Read [this](https://github.com/charliewolf/pynder/issues/171) to get your Token. If you really have trouble, you can message me. 

If you want to use the model trained on my female preferences, you can now just run `bot.py`.

If you want to train your own model, there are additional steps you'll need to follow:

1. Use img_scrape.py to access Tinder through your terminal. When running the program, press 1 to dislike or 2 to like. Do this for thousands of images.

2. Once you have your dataset, run `prepare_data.ipynb` to extract the faces from the images. Save as a numpy file. Aim for 3000 use-able images for decent performance.

3. I wouldn't recommend training the cNN on your PC. You'll need to start a deep learning server using AWS or Google Cloud. On AWS, I used the Deep Learning AMI t2.medium. 

4. Once you're done training, you need to export your model as an h5 file. Transport this h5 file into the bot. Within `bot.py`, find the `load_model()` function and plug the name of your file into that functino.

5. Voila, you should be good to go! 

