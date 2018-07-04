# SBIR
Sketch Based Image Recognition System


<h3>Overview</h3>

Image-based search is a valuable tool that is closely tied to the computer vision problem of object recognition and classification. In a system that performs image searches, it is desirable both to find close image matches and to classify a query image. Often, however,a user may not have a digital photograph of an object for which he or she desires to perform a search. In this case, it is desirable that the user be able to perform the search using a rough sketch of the desired object.
Our system is focused on the specific problems of matching sketched query images to a database of sketches and classifying those query images. The work is meaningful because it demonstrates the potential of the computer to classify and compare hand-drawn sketches,
which are imperfect and sparse relative to actual photos.

Software Requirements
-------------------
Python 2.7 environment with modules like cv2(Open-CV), numpy, Tkinter, pickle and PIL installed.

USAGE
------
The `gui.py` is the main application file through which you would run the application. Opening the application you would get a paint kind of small window where you can draw your sketch. After drawing the sketch you just need to click the process button to get the most similar image to your sketch from your collection of images. 

The folder `sample_images` will contain the images that will be processed by using the `detect.py` file. It is a request to add images by the name of sequence numbers from 0 to whichever number of images you want to place in the folder. Also for now it contains a sample of five png images from 0 to 5. Just edit the range of numbers after adding the images in the `detect.py` file and you are ready to find the local and global features of all the images you added which would be safely stored in local.txt and global.txt files respectively.

The `compare.py` helps the application in comparision of your sketch features with the features of all the other images and producing the best image nearest to the sketch drawn.


WORKING PRINCIPLE
---------------------
We find out the local and global features of the image by running a canny based edge detection algorithm for every image to extract its edges. After we received the edges of the image we ran a edge histogram descriptor that stores description about the kind of edges contained in the image. For the same purpose we divide the entire image into sub images and then classify the edges into different categories viz; horizontal,vertical,135 degree, 45 degree and non-directional edge. The information about these at different parts of image constitutes the local features. For the globalfeature we add all the categories of edges in all sub-images. 
Once the `detect.py` file is run, it processes all the images and store its local and global features in the local.txt andd global.txt files. After that we use our gui to draw the sketch and process it to get the nearest matching image.

Applications & Future Scope
----------------------------
The utility of derieving images from sketches finds many utility like image searching, crime prevention. In the area of education, young children could learn to draw objects in a computer game that automatically evaluates the category of the sketched object. The application could be extended to handheld devices and merged with popular search engines and drawing tools where drawing sketches to find images would be highly convenient.

<br><br>

Hope you will enjoy running the application and you will find it informative to learn about computer vision and its scope.
