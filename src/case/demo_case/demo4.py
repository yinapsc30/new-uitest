import requests

url = 'http://test.coupert.com/api/v2/ext/serviceClick?guid=adfa5aa6e0a5f79267ccedc0da34c2df&lang=en&activity_lang=en'

data_json = {
    "cid": "15606146871586491930",
    "o_domain": "amazon.com",
    "o_title": "LipLoveLine Soft Matte Liquid Lipsticks, 5 ML (Nude Brown Ask)",
    "o_price": 15,
    "o_url": "https://www.amazon.com/dp/B09RND2RC5/ref=va_live_carousel?pf_rd_r=YC1MY7GT32AX02AV1PZK&pf_rd_p=007462d9-ff00-4aeb-b495-e07a9b9c9cfd&pf_rd_m=ATVPDKIKX0DER&pf_rd_t=Gateway&pf_rd_i=desktop&pf_rd_s=desktop-editorial&linkCode=ilv&tag=onamzvikitaea-20&ascsubtag=Highlighting_Amazing_Black_owned_businesses_230110014205&asc_contentid=amzn1.amazonlive.broadcast.caf97ba4-6b81-4578-acdb-cc92b116b2e2&pd_rd_i=B09RND2RC5&th=1",
    "pic_url": "https://m.media-amazon.com/images/I/61u7ieeowkL._SY741_.jpg",
    "upc": "850039400070",
    "mpn": "",
    "isbn10": "",
    "isbn13": "",
    "brand": "LipLoveLine",
    "category": "Beauty&PersonalCare›Makeup›Lips›Lipstick",
    "description": "Velvety-soft and super smooth     Highly Pigmented     Vegan, cruelty-free, non-toxic     Free of gluten, parabens, and sulfates     Jojoba Seed Oil - forms a barrier that effectively locks moisture in and protects your lips from harsh weather conditions, keeping them soft and supple     Pomegranate Flower Extract - presents healing and anti-inflammatory properties",
    "availability": "In Stock.",
    "size": "",
    "color": "Nude Brown",
    "style": "",
    "price_curr": 15,
    "price_was": "",
    "currency": "$",
    "shipping_info": "FREE delivery Sunday, January 15 on $25 of items shipped by Amazon",
    "condition": "",
    "country": "",
    "tax": "",
    "errorFields": [],
    "price_all": "$15.00",
    "position": "left",
    "symbol": "$",
    "list": [
        {
            "title": "Maybelline Color Sensational Ultimatte Slim Lipstick - More Taupe",
            "store_name": "Ulta Beauty",
            "description": "最晚于 1月24日周二送达, 满 US$35免运费, 60 天内可退货, Members earn points & more  “Ultimate Rewards”会员福利Members earn points & moreBronze可随意加入Join NowEarn 1 Point Per $1 SpentFree Birthday Coupon$5 Off Coupon For Next OrderEarn Points On Every PurchaseEarn 2x Points In Birthday MonthFree Mag & Coupons MailedPoints Redeemable On All ItemsPlatinum消费达到 US$500.00Join NowEarn 1.25 Points Per $1 SpentFree Birthday CouponExclusive DealsGiftEarly AccessIncrease Your Rewards At PlatinumEarn 2x Points In Birthday MonthDiamond消费达到 US$1,200.00Join NowEarn 1.5 Points Per $1 Spent​​ Free Diamond Gift​​ Free Standard Shipping $25 Min.​​ Earn Points On Every Purchase​​ $25 Services Reward​​ Exclusive Diamond Offers​​ Earn 2x Points In Birthday Month​​ Points Redeemable On All Items某些福利尚无法在 Google 上获取，某些商家也尚未在 Google 上线。",
            "price_all": "US$9.49",
            "price": 9.49,
            "position": "left",
            "symbol": "US$",
            "total_price": 18,
            "domain": "amazon.com",
            "url": "https://www.ulta.com/p/color-sensational-ultimatte-slim-lipstick-pimprod2020630?sku=2574440&CMPID=CSGGLE&CAWELAID=330000200002705292&srsltid=AeTuncp4VtRWS7u6U7HRu8olZAatLehq5Z-HZVd9_To4K6QNpdVVbIYgl7Q&sa=U&ved=0ahUKEwiY5bqQ9rv8AhXvnGoFHawICycQ1ykIMA&usg=AOvVaw2hoNgSFUOcq-yIgz9WpkSx",
            "match_type": 2,
            "target_domain": "ulta.com"
        },
        {
            "title": "Maybelline Color Sensational Ultimatte Slim Lipstick - More Taupe",
            "store_name": "Ulta Beauty",
            "description": "204.3英里 · San Leandro有货今天： 上午10:00 - 下午8:00",
            "price_all": "US$9.49",
            "price": 9.49,
            "position": "left",
            "symbol": "US$",
            "total_price": 9.49,
            "domain": "amazon.com",
            "url": "https://www.ulta.com/p/color-sensational-ultimatte-slim-lipstick-pimprod2020630?sku=2574440&CMPID=CSGGLE&CAWELAID=330000200002705292&sa=U&ved=0ahUKEwiY5bqQ9rv8AhXvnGoFHawICycQ1ykIOQ&usg=AOvVaw1b9tjmJfeomotVJbGePHQ8",
            "match_type": 2,
            "target_domain": "ulta.com"
        },
        {
            "title": "Maybelline Color Sensational Ultimatte Slim Lipstick - More Taupe",
            "store_name": "CVS Pharmacy",
            "description": "202.1英里 · Hayward有货今天： 上午9:00 - 下午8:00",
            "price_all": "US$9.79",
            "price": 9.79,
            "position": "left",
            "symbol": "US$",
            "total_price": 9.79,
            "domain": "amazon.com",
            "url": "https://www.cvs.com/shop/maybelline-color-sensational-ultimatte-slim-lipstick-makeup-prodid-2940025?skuid=789625&cgaa=QWxsb3dHb29nbGVUb0FjY2Vzc0NWU1BhZ2Vz&sa=U&ved=0ahUKEwiY5bqQ9rv8AhXvnGoFHawICycQ1ykIXg&usg=AOvVaw3150xjAHyCY362YJh3KdR4",
            "match_type": 2,
            "target_domain": "cvs.com"
        },
        {
            "title": "Maybelline Color Sensational Ultimatte Slim Lipstick - More Taupe",
            "store_name": "Walgreens.com",
            "description": "208.6英里 · Los Gatos有货今天： 上午8:00 - 下午10:00",
            "price_all": "US$9.49",
            "price": 9.49,
            "position": "left",
            "symbol": "US$",
            "total_price": 9.49,
            "domain": "amazon.com",
            "url": "https://www.walgreens.com/store/c/maybelline-color-sensational-ultimatte-slim-lipstick-makeup/ID=300409480-product?sa=U&ved=0ahUKEwiY5bqQ9rv8AhXvnGoFHawICycQ1ykIgwE&usg=AOvVaw274hcRQF4sl2bQXzlkXnKx",
            "match_type": 2,
            "target_domain": "walgreens.com"
        },
        {
            "title": "Maybelline Color Sensational Ultimatte Slim Lipstick - More Taupe",
            "store_name": "Walmart",
            "description": "214.5英里 · Tracy有货今天： 上午6:00 - 下午11:00",
            "price_all": "US$7.48",
            "price": 7.48,
            "position": "left",
            "symbol": "US$",
            "total_price": 7.48,
            "domain": "amazon.com",
            "url": "https://www.walmart.com/ip/Maybelline-Color-Sensational-Ultimatte-Slim-Lipstick-Makeup-More-Taupe-0-06-oz/318395480?wl13=2025&selectedSellerId=0&sa=U&ved=0ahUKEwiY5bqQ9rv8AhXvnGoFHawICycQ1ykIkAE&usg=AOvVaw1xqN6b2PPt7Zh6obY3DMjF",
            "match_type": 2,
            "target_domain": "walmart.com"
        },
        {
            "title": "Maybelline Color Sensational Ultimatte Slim Lipstick - More Taupe",
            "store_name": "Walmart",
            "description": "运费为 US$6.99, 90 天内免费退货",
            "price_all": "US$7.48",
            "price": 7.48,
            "position": "left",
            "symbol": "US$",
            "total_price": 15.84,
            "domain": "amazon.com",
            "url": "https://www.walmart.com/ip/Maybelline-Color-Sensational-Ultimatte-Slim-Lipstick-Makeup-More-Taupe-0-06-oz/318395480?wmlspartner=wlpa&selectedSellerId=0&sa=U&ved=0ahUKEwiY5bqQ9rv8AhXvnGoFHawICycQ1ykItgE&usg=AOvVaw1VyWEzrNBWLUyvxutYNsR9",
            "match_type": 2,
            "target_domain": "walmart.com"
        },
        {
            "title": "Maybelline Color Sensational Ultimatte Slim Lipstick - More Taupe",
            "store_name": "Target",
            "description": "205.3英里 · San Mateo有货今天： 上午8:00 - 下午10:00",
            "price_all": "US$7.49",
            "price": 7.49,
            "position": "left",
            "symbol": "US$",
            "total_price": 7.49,
            "domain": "amazon.com",
            "url": "https://www.target.com/p/maybelline-color-sensational-ultimatte-slim-lipstick-799-more-taupe-0-06oz/-/A-79858520?ref=tgt_adv_XS000000&AFID=google_pla_df_free_local&CPNG=Beauty&adgroup=52-7&sa=U&ved=0ahUKEwiY5bqQ9rv8AhXvnGoFHawICycQ1ykIvwE&usg=AOvVaw0szbTkzQwrXTK7MIvZg2XS",
            "match_type": 2,
            "target_domain": "target.com"
        },
        {
            "title": "Maybelline Color Sensational Ultimatte Slim Lipstick - More Taupe",
            "store_name": "Target",
            "description": "最晚于 1月18日周三送达, 90 天内可退货, Members earn exclusives & free shipping  “Target”会员福利Members earn exclusives & free shippingTarget Circle™可随意加入Join NowEarn 1% when you shop plus exclusive offers on eligible items for membersGet a birthday gift on your big dayEarn votes to help direct where Target gives in your communityRestrictions apply. Visit target.com/circle to learn moreTarget RedCard™RedCard™Apply Now5% off everyday at Target & free shipping on eligible items for membersAdditional 30 days for returnsRedCard™ exclusives: special items gifts and offersRestrictions apply. Visit target.com/redcard to learn more某些福利尚无法在 Google 上获取，某些商家也尚未在 Google 上线。",
            "price_all": "US$7.49",
            "price": 7.49,
            "position": "left",
            "symbol": "US$",
            "total_price": 8.2,
            "domain": "amazon.com",
            "url": "https://www.target.com/p/maybelline-color-sensational-ultimatte-slim-lipstick-799-more-taupe-0-06oz/-/A-79858520?ref=tgt_adv_XS000000&AFID=google_pla_df_free_online&CPNG=Beauty&adgroup=52-7&sa=U&ved=0ahUKEwiY5bqQ9rv8AhXvnGoFHawICycQ1ykI6AE&usg=AOvVaw3H0cB4--LvQHADwk6tFYhg",
            "match_type": 2,
            "target_domain": "target.com"
        },
        {
            "title": "Maybelline Color Sensational Ultimatte Slim Lipstick - More Taupe",
            "store_name": "Rite Aid",
            "description": "235.3英里 · Santa Rosa有货今天： 上午8:00 - 下午9:00",
            "price_all": "US$8.99",
            "price": 8.99,
            "position": "left",
            "symbol": "US$",
            "total_price": 8.99,
            "domain": "amazon.com",
            "url": "https://www.riteaid.com/shop/maybelline-color-sensational-ultimatte-slim-lipstick-more-taupe-799-0-06-oz?utm_source=google&utm_medium=organic&utm_campaign=tinuiti_organicshopping&sa=U&ved=0ahUKEwiY5bqQ9rv8AhXvnGoFHawICycQ1ykI8QE&usg=AOvVaw2qg50V5yPRLePY3kp6WXin",
            "match_type": 2,
            "target_domain": "riteaid.com"
        },
        {
            "title": "Maybelline Color Sensational Ultimatte Slim Lipstick - More Taupe",
            "store_name": "Instacart",
            "description": "运费为 US$11.00，最晚于 1月12日周四送达",
            "price_all": "US$10.49",
            "price": 10.49,
            "position": "left",
            "symbol": "US$",
            "total_price": 23.53,
            "domain": "amazon.com",
            "url": "https://www.instacart.com/landing?product_id=22973635&retailer_id=1573&utm_term=pbi-0&utm_campaign=maybelline-slim-lipstick%2C-non-drying-matte-lipstick-makeup%2C-more-taupe---0.06-oz._walgreens&utm_source=instacart_google&utm_medium=shopping_free_listing&utm_content=productid-22973635_retailerid=1573&region_id=39262239607&sa=U&ved=0ahUKEwiY5bqQ9rv8AhXvnGoFHawICycQ1ykIkAI&usg=AOvVaw0Dtcex6Ab_cEbqK4nyTvnS",
            "match_type": 2,
            "target_domain": "instacart.com"
        }
    ],
    "match_type": 2,
    "language": "zh-CN",
    "cache_time_get_product": 120000
}


headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "cookie": "_iclcs_=1; _trdck=eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNDg4NjUxNyIsInR5cGUiOiJQQyIsIm9zIjoiTWFjaW50b3NoIiwiYnJvd3NlciI6IkNocm9tZSIsImNvbnN1bWVyS2V5IjoiQ291cGVydC5jb20iLCJpc3N1ZWRBdCI6MTY3MzI2NzM0NX0.UHgZ3A24Q6EcWNb8T_5QrQWP7T3sSOOxL_b_TOBGpY4",
}
# res = requests.post(url=url, data=data_json, headers=headers)
#
# reditList = res.history
#
# print(reditList)
# print(res.json())

cb_list = ['FirstPage', 'Popup_Item', 'Popup_Override', 'Popup_ATOverride', 'Injected', 'Inject_Item', 'Icon_Override',
 'FloatWin', 'Popup_ATSaved', 'Popup_ATNoSaving', 'Popup_SATResult']
for cb in cb_list:
    res = requests.post(url=url, data=data_json, headers=headers)
