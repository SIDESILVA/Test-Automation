import itertools

# -------------------- IMAGE URL LIST --------------------
IMAGES = [
    "https://images.immediate.co.uk/production/volatile/sites/30/2023/01/Maqlooba-4cd95c3.jpg?quality=90&resize=708,643",
    "https://pastrieslikeapro.com/wp-content/uploads/2014/09/fresh-as-a-daisy-doughnuts-3.jpg",
    "https://handletheheat.com/wp-content/uploads/2022/06/angel-food-cake-with-berries-SQUARE.jpg",
    "https://www.innovamarketinsights.com/wp-content/uploads/2023/10/soft-drinks--jpg.webp",
    "https://valampuri.foodorders.lk/images/food/phpxpdKKq.jpg",
    "https://img.delicious.com.au/MQnnlDkF/del/2024/05/devilys-food-cake-212625-2.jpg",
    "https://www.thisvivaciouslife.com/wp-content/uploads/2023/06/20-Minute-Gluten-Free-Donuts-Fried-Bakery-Style-square.jpg",
    "https://thai-foodie.com/wp-content/uploads/2025/04/thai-curry-fried-rice-plated.jpg",
    "https://dailyglobalbites.com/_next/image?url=%2Fimages%2Frecipes%2Fkottu%2Fslk1.jpg&w=3840&q=75",
    "https://static01.nyt.com/images/2025/04/15/multimedia/MC-Dark-Chocolate-Pudding-ctqg/MC-Dark-Chocolate-Pudding-ctqg-mediumSquareAt3X.jpg",
    "https://d2td6mzj4f4e1e.cloudfront.net/wp-content/uploads/sites/9/2019/04/soft-drinks.jpg",
    "https://static01.nyt.com/images/2014/05/14/dining/14REDVELVET/14REDVELVET-superJumbo-v4.jpg",
    "https://tuktuknegombo.com/wp-content/uploads/2024/11/Seafood-Kottu-Negombo.webp",
    "https://www.foodandwine.com/thmb/RYsqVqa6snK1_WkmZm7m-h6rwfM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/FAW-recipes-double-chocolate-pudding-hero-f8cf686f09504feb8b155c4c2c459838.jpg",
    "https://rakskitchen.net/wp-content/uploads/2021/04/vegan-mango-pudding-feature.jpg",
    "https://i.ytimg.com/vi/YpZoIAvnkBw/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLB6-oIsOOLjJ2DC6Yr-1CUoLBoR6g",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVPvcZIxeA9bZukK18CymY32OqFUTVbkKXgQ&s",
    "https://img.freepik.com/premium-photo/close-up-cold-refreshing-soft-drink_79782-1212.jpg?w=360",
    "https://images.immediate.co.uk/production/volatile/sites/30/2020/12/Noodles-with-chilli-oil-eggs-6ec34e9.jpg?quality=90&resize=708,643",
    "https://japanesecooking101.com/wp-content/uploads/2013/10/IMG_7721.jpg",
    "https://www.marthastewart.com/thmb/mcD5yGPCx_n2FFqJfUzBOdEAX98=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/MS_31523_Lemony_Angel_Food_Cake_Hero-0417da898247478baa5f68a66e1ad87d.jpg",
    "https://tb-static.uber.com/prod/image-proc/processed_images/b895a684f043c79d93790099b39bd22c/c73ecc27d2a9eaa735b1ee95304ba588.jpeg",
    "https://blog.cinnamonhotels.com/wp-content/uploads/2022/03/shutterstock_446312773.jpg",
    "https://www.shutterstock.com/image-photo/soft-drinks-fruit-juice-mixed-600nw-2699110919.jpg",
    "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/chorizo-mozarella-gnocchi-bake-cropped-9ab73a3.jpg",
    "https://i.pinimg.com/originals/1b/0d/14/1b0d1416ec40aa636a6eccda02522ec9.png",
    "https://static.independent.co.uk/s3fs-public/thumbnails/image/2018/01/12/12/healthy-avo-food.jpg",
    "https://images.immediate.co.uk/production/volatile/sites/30/2022/06/Party-food-recipes-fcfb3af.jpg?quality=90&resize=708,643",
    "https://hips.hearstapps.com/hmg-prod/images/cranberry-sauce-spritz-lead-web-077-rl-del079925-690cc67f21793.jpg?crop=1xw:1xh;center,top",
    "https://www.americanafoods.com/wp-content/uploads/2024/07/shutterstock_1291051588-min-1.jpg",
    "https://img.magnific.com/free-photo/penne-pasta-tomato-sauce-with-chicken-tomatoes-wooden-table_2829-19739.jpg?semt=ais_hybrid&w=740&q=80",
    "https://www.kimscravings.com/wp-content/uploads/2022/04/Better-Than-Sex-Cake-7.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOpUxpdgh4JkrP0PumMmoJ2w1Zt-cinDi4LA&s",
    "https://images.immediate.co.uk/production/volatile/sites/30/2022/06/Tequila-sunrise-fb8b3ab.jpg",
    "https://blog.travelkhana.com/tkblog/wp-content/uploads/sites/2/2023/02/A-to-Z-Food-1024x683.jpg",
    "https://www.thespruceeats.com/thmb/n0Qrw_zVBuaDzIJGBBMrk1ainBs=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/custard-pudding-recipes-2031113-hero-01-5727ccf9942b402897c493fd09bae739.jpg",
]

# -------------------- ROTATION --------------------
_cycle = itertools.cycle(IMAGES)

def get_next_image_url():
    """
    Returns next image URL in rotation (NO download needed)
    """
    return next(_cycle)