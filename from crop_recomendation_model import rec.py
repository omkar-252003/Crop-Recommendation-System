from crop_recomendation_model import recommend_crop

crop,temp,hum,rain=recommend_crop(104,18,30,6.7,"bangalore")
crop_info = {
            'temperature': temp,
            'humidity': hum,
            'rainfall': rain,
            'recommended_crop': crop,
            'image': crop+".jpeg"
        }
print(crop_info)