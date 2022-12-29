#real world example
import requests
import time
img_urls=["https://images.pexels.com/photos/3408744/pexels-photo-3408744.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
          "https://images.pexels.com/photos/624015/pexels-photo-624015.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"]
start=time.perf_counter()
for img_url in img_urls:
    img_bytes=requests.get(img_url).content
    img_name=img_url.split('/')[4]
    img_name=f'{img_name}.jpg'
    with open(img_name,'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name}was downloaded')
finish=time.perf_counter()
print(f'Finish in{finish-start} seconds')