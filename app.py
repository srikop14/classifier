
import streamlit as st
import base64
import requests
from PIL import Image
import io

#################################
#needful functions

#to resize images
# def image_resizer(image1, image2):
#   #first image
#   #second image will be resized bbased on image1 dimension
#   img1 = Image.open(image1)
#   size1 = img1.size[0]
#   size2 = img1.size[1]

#   #resizing the second image
#   img2 = Image.open(image2)
#   img3 = img2.resize((size1, size2))
#   img3.show()
#   return img3

#to get predictions
def get_prediction(image_data):
  #replace your image classification ai service URL
  url = 'https://askai.aiclub.world/95a1f13d-8106-4fa2-95ba-8e581761cda9'
  r = requests.post(url, data=image_data)
  response = r.json()['predicted_label']
  return response

#################################
#creating the web app

#title for the web app
st.title("🐱 Cats & Dogs Classifier 🐶")

#subheader
st.subheader("About the projct..")
#write elements 
st.write("**This web can be used to classify images of cats and dogs. AI was trained in Navigator with AI Club datasets.**")

#showing cats images
st.image("cats.jpg", caption = "Picture of cats")

#showing dogs images
st.image("dogs.jpg", caption = "Picture of dogs")


#file uploading and prediction part

image = st.file_uploader(label="Upload an image",accept_multiple_files=False, help="Upload an image to classify them")
if image:
    #converting the image to bytes
    img = Image.open(image)

    #image to be predicted
    st.image(img, caption = "Image to be predicted")

    #converting the image to bytes
    buf = io.BytesIO()
    img.save(buf,format = 'JPEG')
    byte_im = buf.getvalue()

    #converting bytes to b64encoding
    payload = base64.b64encode(byte_im)

    #file details
    file_details = {
      "file name": image.name,
      "file type": image.type,
      "file size": image.size
    }

    #write file details
    st.write(file_details)

    #predictions
    response = get_prediction(payload)

    #prediction label
    st.markdown("This is a **{}**".format(response.split('s')[0]))
