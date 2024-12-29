import streamlit as st
from PIL import Image
import subprocess


try:
    st.set_page_config(
        page_title="CRISPAN SUITE & EVENT CENTER JOS",
        layout="centered",
        page_icon="icon.ico"  # Ensure this file exists in the working directory
    )
except Exception as e:
    st.warning(f"Page icon could not be set. Error: {e}")
# Data for menu items and their components
menu_data = {
    "BLACK TEA": {
        "Tea 2 GRAM": 117.00,
        "Brown Sugar 2 GRAM": 3.40,
    },
    "MANGO TEA": {
        "TEA POWDER 2 GRAM": 117.00,
        "SUGAR 2.5 GRAM": 3.40,
        "LEMON 2 ML": 20.0,
        "MANGO 5 ML": 25.0,
    },
    "LEMON TEA": {
        "LEMON (FRUIT) 10 ML": 50,
        "TEA POWDER 8 GRAM": 117,
        "HONEY/SUGAR 4 GRAM": 3.4,
    },
    "STRAWBERRY TEA": {
        "STRAWBERRY 4 ML": 266,
        "GREEN TEA 4 GRAM": 117,
        "HONEY/SUGAR 15 GRAM": 26,
    },

    "PEACH TEA": {
        "TEA 2 GRAM": 117,
        "PEACH 20 ML": 200,
        "SUGAR 2 GRAM": 3.4,
      },

    "BLUE BERRY  TEA": {
        "SUGAR 4 GRAM": 7.00,
        "GREEN TEA 2 GRAM": 117.00,
        "BLUE BERRY 4 ML": 266,
      },

    "PLAIN OMELLETE": {
        "EGG 2 PCS": 300.00,
        "SALT 0.5 GRAM": 0.25,
        "PEPPER 5 GRAM": 4.7,
        "VEGETABLE OIL 15 ML": 218.00,
    },

    "SARDINE OMELLETE": {
        "EGG 2 PCS": 300.00,
        "SALT 0.5 GRAM": 0.25,
        "PEPPER 5 GRAM": 4.70,
        "SARDINE 80 GRAM": 440.00,
        "ONIONS 30 GRAM": 26,
        "VEGETABLE OIL 15 ML": 218,
    },

    "POACHED EGG": {
        "EGG 1 PCS": 150.00,
        "SALT 0.5 GRAM": 0.25,
        "VINEGAR 15 ML": 10.8,
     },

    "SPANISH OMELLETE": {
        "CARROT 10 GRAM": 21.6,
        "ONION 10 GRAM": 13.00,
        "OLIVE OIL 15 ML": 218,
        "EGG 2 PCS": 300.00,
        "SALT 0.5 GRAM": 0.25,
        "GREEN BEANS 10 GRAM": 13.00,
        "FRESH TOMATOES 10 GRAM": 4.00,
        "PEPPER (OPTIONAL) 5 GRAM": 4.70,
    },

    "SCRAMBLED EGG": {
        "EGGS 3 PCS": 450.00,
        "MILK 4 GRAM": 26.00,
        "SALT 0.5 GRAM": 0.25,
        "BUTTER 15 gram": 94.00,
        "WHITE PEPPER (OPTIONAL) 0.5 gram": 20.80,
    },

    "CHEESE OMELLETE": {
        "EGGS 3 PCS": 450.00,
        "PEPPER (OPTIONAL) 5 GRAM": 4.70,
        "SALT 2 GRAM": 2.00,
        "OLIVE OIL 15 ML": 218,
        "MOZOROLLA CHEESE 10 GRAM": 550,
    },

    "BOILED EGG": {
        "EGGS 1 PCS": 150.00,
        "WATER": 10.00,
    },

    "QUEENS OMELLETE": {
        "EGGS 3 PCS": 450.00,
        "PEPPER 5 GRAM": 4.7,
        "SALT 2 GRAM": 2.00,
        "HOT CHILLI 15 GRAM": 75.00,
        "GREEN BEANS 10 GRAM": 13.00,
        "OLIVE OIL 15 ML": 218.00,
        "CARROT 10 GRAM": 4.00,
        "LEEK 5 GRAM": 38.00,
        "CHICKEN 40 GRAM": 128.00,
    },

    "JOLLOF RICE": {
        "RICE 180 GRAM": 306.00,
        "VEGETABLE OIL 30ML": 63.6,
        "TUMERIC PASTE 2.5 GRAM": 0.31,
        "SHUMBO PASTE 15 GRAM": 70.00,
        "KNORR CUBE 2GRAM": 21.5,
        "ONIONS 20 GRAM": 10.77,
        "TOMATOE PASTE 30 GRAM": 34.37,
        "BLENDED RAW TOMATOES 60 GRAM": 68.7,
        "BAY LEAF 0.5 GRAM": 2.00,
        "SALT  0.5 gram": 0.38,
        "CURRY 2 GRAM": 12.00,
        "THYME 2 GRAM": 12.00,
        "GARLIC 2 GRAM": 0.11,
        "FRESH PEPPER 4 GRAM": 13.8,
        "MEAT STOCK 1 CUP": 50.00,
    },

    "NATIVE RICE": {
        "RICE 180 GRAM": 306,
        "DRY FISH 40 GRAM": 371.4,
        "PALM OIL 75 ML": 102,
        "CRAYFISH 15 GRAM": 75.00,
        "KNORR CUBE 12 GRAM": 21.5,
        "FRESH TOMATOES 300 GRAM": 315,
        "ONIONS 50 GRAM": 27.00,
        "SPINACH 100 GRAM": 50.00,
        "PEPPER 5 GRAM": 17.31,
    },

    "NIGERIAN FRIED RICE": {
        "RICE 180 GRAM": 306.00,
        "VEGETABLE OIL 75 ML": 159.00,
        "SEASONING CUBE 4 GRAM": 43.00,
        "SALT 3 GRAM": 1.13,
        "GARLIC 2 GRAM": 0.11,
        "ONIONS 20 GRAMS": 10,
        "SHUMBO (BELL PEPPER) DICED ": 37.3,
        "CURRY 2GRAM": 11.7,
        "TUMERIC 2.5 GRAM": 0.31,
        "GREEN BEANS 10 GRAM": 43,
        "SWEET CORN 10 GRAM": 41.6,
        "CARROTS 10 GRAM": 7.00,
    },

    "ACHA FLOUR/ACHA GRAIN": {
        "FLOUR 130grram": 317.7,
        "GRAIN 50gram": 116.7,
       
    },

    "COCONUT RICE": {
        "RICE 180 GRAM": 306.00,
        "DRY FISH 40 GRAM": 371.4,
        "VEGETABLE OIL 45 ML": 95.4,
        "ONIONS 20 GRAM": 10.00,
        "CRAYFISH 7.5 GRAM": 37.5,
        "COCONUT POWDER 10 GRAM": 75,
        "DRY PEPPER 2 GRAM": 13.7,
        "SEASONING CUBE 4 GRAM": 86.00,
               
    },

    "WHITE RICE & STEW": {
        "RICE 180 GRAM": 306.00,
        "GREEN BEANS 10 GRAM": 43.00,
        "CARROT 10 GRAM": 16.00,
        "FRESH TOMATOES 100 GRAM": 105.00,
        "ONIONS 30 GRAM": 40.8,
        "TOMATOE PASTE 15 GRAM": 34.4,
        "KNORR CUBE 2 GRAM": 21.5,
        "VEGETABLE OIL 75ML": 159,
        "CURRY 1.2 GRAM": 13.2,
        "THYME 0.5 gram": 1.38,
        "SALT 0.5 gram": 1.34,
        "SHUMBO 50 GRAM": 233.00,
        "GARLIC 5 GRAM": 0.28,
        "FRESH PEPPER 4GRAM": 43.00,
    },

    "OHA SOUP": {
        "OFFALS  15 GRAM": 55.00,
        "KPOMO 62.5 GRAM": 62.5,
        "CRAYFISH 4 GRAM": 20.00,
        "STOCK FISH 40 GRAM": 334.6,
        "DRY FISH 40 GRAM": 371.4,
        "PALM OIL 60ML": 81.6,
        "OHA LEAF 50 GRAMS": 100.6,
        "EDE (COCOYAM) 80 GRAMS": 133.4,
        "FRESH PEPPER 8 GRAM": 27.7,
        "OGIRI 10 GRAM": 40.0,
        "UZIZA LEAF 10 GRAMS": 40,
        "KNORR CUBE 4 GRAM": 43,
    },

    "AFANG SOUP": {
        "STOCK FISH 40 GRAM": 334.6,
        "DRY FISH 40 GRAM": 371.4,
        "OFFALS 15 GRAM": 55,
        "PERIWINKLE 10 GRAMS": 150.00,
        "CRAYFISH 4 GRAM": 20.00,
        "KPOMO 62.5 GRAMS": 62.5,
        "AFANG LEAF 20 GRAMS": 80.00,
        "WATER LEAF 200 GRAMS": 60.00,
        "PALM OIL 75ML": 102.00,
        "ONIONS 20 GRAMS": 27.00,
        "BLENEDED PEPPER 8 GRAM": 27.7,
        "KNORR CUBE 4 GRAM": 43.00,
        
    },

    "VEGETABLE SOUP": {
        "STOCK FISH 40 GRAM": 334.6,
        "KPOMO 62.5 GRAMS": 62.5,
        "OFFALS 15 GRAM": 55.00,
        "DRY FISH 30 GRAM": 279,
        "CRAYFISH 4 GRAM": 20,
        "ONIONS 20 GRAM": 27.2,
        "UGU LEAF 100 GRAM": 200,
        "WATER LEAF 200 GRAM": 60,
        "PALM OIL 90 ML": 122.4,
        "RED PEPPER 5 GRAM": 17.31,
        "KNORR CUBE 0.5 GRAMS": 1.34,
        
    },

    "BITTER LEAF SOUP": {
        "OFFALS 15 GRAM": 55.00,
        "DRY FISH 40 GRAMS": 371.4,
        "STOCK FISH 40 GRAM": 334.6,
        "KPOMO 62.5 GRAMS": 62.5,
        "CRAYFISH 4 GRAM": 20,
        "BITTER LEAF 40 GRAM": 80,
        "ONIONS 30 GRAM": 40.8,
        "PALM OIL 90 ML": 122.4,
        "COCOYAM (EDE) 80 GRAMS": 133,
        "OGIRI 10 GRAMS": 40,
        "BLENDED PEPPER 4 GRAM": 13.8,
        "KNORR CUBE 4 GRAM": 43,
        
    },

    "OGBONNO SOUP": {
        "OFFALS 15 GRAM": 55.00,
        "DRY FISH 30 GRAMS": 279,
        "KPOMO 62.5 GRAMS":62.5,
        "STOCK FISH 40 GRAM": 334.6,
        "CRAYFISH 4 GRAM": 20,
        "OGBONNO 20 GRAMS": 260,
        "PALM OIL 75ML": 102,
        "UZIZA LEAF 10 GRAM": 40,
        "UGU LEAF 40 GRAM": 80,
        "ONIONS 20 GRAMS": 27,
        "PEPPER  4 GRAM": 13.8,
        "KNORR CUBE 4 GRAM": 43,
        
    },

    "EGUSI SOUP": {
        "OFFALS 15 GRAM": 55.00,
        "KPOMO 62.5 GRAMS": 62.5,
        "DRY FISH 30 GRAMS": 279,
        "STOCK FISH 30 GRAM": 251,
        "CRAYFISH 4 GRAM": 20,
        "EGUSI 100 GRAM": 300,
        "PALM OIL 105ML": 149,
        "ONIONS 20 GRAM": 27.2,
        "UGU 30 GRAM": 60,
        "UZIZA LEAF 5 GRAM": 20,
        "BLENDED PEPPER 4 GRAM": 43,
        "KNORR CUBE 2 GRAM": 21.5,
        
    },

    "WHITE SOUP": {
        "DRY FISH 40 GRAM": 371.4,
        "OFFALS 30 GRAM": 110,
        "STOCK FISH 40 GRAM": 334.6,
        "KPOMO 62.5 GRAMS": 125,
        "YAM 105 GRAM": 174.5,
        "ONIONS 10 GRAM": 13.6,
        "VEG. OIL 15 ML": 31.8,
        "FRESH PEPPER 4 GRAM": 43,
        "KNORR CUBE 4 GRAM":43,
        "CRAYFISH 4 GRAM": 20,
        "UDA 2 GRAM": 10,
        "UZIZA LEAF 10 GRAM": 40,
        "UZIZA SEED 2 GRAM": 10,
        "SALT 0.5 GRAM": 1.34,
        
    },

    "OKRO SOUP": {
        "OKRO SOUP 50 GRAMS": 45.8,
        "PALM OIL 75ML": 102,
        "ONIONS 10 GRAMS": 13.6,
        "PEPPER 4 GRAMS": 13.8,
        "UGU 20 GRAMS": 40,
        "CRAYFISH 4 GRAM": 20,
        "KPOMO 62.5 GRAMS": 62.5,
        "KNORR CUBE 4 GRAM": 43,
        "SALT 0.5 GRAMS": 1.34,
        "UZIZA LEAF 20 GRAMS": 80,
        "OFFALS 15 GRAM": 55,
        "STOCK FISH 30 GRAM": 250,
        "DRY FISH 30 GRAMS": 279,
        
    },

    "SEAFOOD OKRO SOUP": {
        "PALM OIL 60 ML": 81.6,
        "ONIONS 20 GRAMS": 27.2,
        "FRESH OKRO 100 GRAMS": 66.6,
        "PERIWINKLE 2 GRAMS": 800,
        "ASSORTED (OPTIONAL) 30 GRAMS": 139.5,
        "STOCKFISH 50 GRAMS": 150,
        "SNAIL 50 GRAMS ": 250,
        "PRAWN 30 GRAMS": 330,
        "FISH 50 GRAMS": 160,
        "KNORR CUBE 0.5 GRAMS": 5.3,
        "UGU LEAF 20 GRAMS": 80,
        "UZIZA 10 GRAMS": 67,
        "NATIVE SPICE (OPTIONAL) 10 GRAMS": 40,
        "DRY FISH 30 GRAMS": 300,
        "FRESH PEPPER 4GRAM": 14,
        "SALT 0.5 GRAMS": 0.25,
    },

    "WHEAT": {
        "FLOUR 180 GRAM": 288,
       
    },

    "GARRI (EBA)": {
        "GARRI 180 GRAM": 202.5,
        "PALM OIL 1 TSP (5ML)": 6.8,
        
    },

    "SEMO": {
        "SEMO 180 GRAM": 221.4,
        
    },

    "AMALA": {
        "FLOUR 180 GRAM": 216,
        
    },

    "POUNDO": {
        "FLOUR 180 GRAM": 414,
        
    },

    "BEANS POTTAGE": {
        "BROWN BEANS 150 GRAM": 308.00,
        "PALM OIL 5 TBL SP (75 ML)": 102.00,
        "ONIONS 20 GRAM": 27.00,
        "FRESH TOMATOES 100 GRAM": 105.00,
        "DRY PEPPER 1 TSP (4 GRAM)": 27.7,
        "SALT 0.5 GRAM": 0.38,
        "CRAYFISH 1 TSP(4 GRAM)": 20,
        "SPRING ONION 50 GRAM": 5.00,
        
    },

    "YAM PORRIDGE": {
        "YAM 300 GRAM": 500.00,
        "DRY FISH 30 GRAM": 279.00,
        "FRESH TOMATOES 100 GRAM": 105.00,
        "ONIONS 20 GRAM": 27.00,
        "PALM OIL 75ML": 102.00,
        "CRAYFISH 4 GRAM": 20.00,
        "DRY PEPPER 4 GRAM": 13.8,
        "KNORR CUBE 4 GRAM": 43.00,
        "STEAM SPINACH 50 GRAM": 25.00,
        "SALT 0.5 GRAM": 0.25,
       
    },

    "FARM HOUSE POTATOE": {
        "Palm Oil 75 ML": 114.00,
        "Onions 50 GRAM": 68.00,
        "Fresh Tomato 100 GRAM": 105.00,
        "Yam 150 GRAM": 212.00,
        "Plantain 150 GRAM": 450.00,
        "Dry Fish 20 GRAM": 200.00,
        "Cray Fish 10 GRAM": 70.00,
        "knorr cube 4 GRAM": 44.00,
        "Salt 0.5 GRAM": 0.25,
        "Pepper 4 GRAM": 3.7,
        "Vegetables 30 GRAM": 90.00,
        
    },

    "UNRIPE PLANTAIN POTTAGE": {
        "Palm Oil 75 ML": 114.00,
        "Onions 50 GRAM": 68.00,
        "Fresh Tomato 100 GRAM": 105.00,
        "Unripe Plantain 300 GRAM": 900.00,
        "Dry Fish 20 GRAM": 200.00,
        "Cray Fish 10 GRAM": 70.00,
        "knorr cube 4 GRAM": 44.00,
        "Salt 0.5 GRAM": 0.25,
        "Pepper 4 GRAM": 3.7,
        "Vegetables 30 GRAM": 90.00,
       
    },

    "LIVER SAUCE": {
        "LIVER (CHOPPED) 250 GRAM": 1500.00,
        "ONIONS (CHOPPED) 50 GRAM": 68.00,
        "PEPPER (CHOPPED) 4 GRAM": 3.7,
        "KNORR CUBE 4 GRAM": 44.00,
        "VEGETABLE OIL 30 ML": 60.00,
        "CURRY 2 GRAM": 12.00,
        "THYME 2 GRAM": 12.00,
        "GREEN PEPPER 4 GRAM": 3.7,
        "YELLOW PEPPER 4 GRAM": 3.7,
        "RED PEPPER 4 GRAM": 3.70,
        "GARLIC 10 GRAM": 55.00,
        "CORN FLOUR 15 GRAM": 32.00,
        "SALT 0.5 GRAM": 0.25,
        
    },

    "VEGETABLE SAUCE": {
        "ONION 50 GRAM": 68.00,
        "CARROTS 100 GRAM": 200.00,
        "RED PEPPER 40 GRAM": 40.00,
        "GREEN PEPPER 150 GRAM": 150.00,
        "CABBAGE 50 GRAM": 166.00,
        "SOY SAUCE 4 ML": 20.00,
        "OYSTER SAUCE 4 ML": 16.00,
        "KNORR CUBE 4 GRAM": 44.00,
        "PEPPER 40 GRAM": 40.00,
        "CORN FLOUR 10 GRAM": 20.00,
        "VEGETABLE OIL 30 ML": 63.00,
        "SALT 2.5 GRAM": 1.25,
       
    },

    "GREEN VEGETABLE SAUCE": {
        "PALM OIL 75 ML": 114.00,
        "ONIONS (CHOPPED) 50 GRAM": 68.00,
        "TOMATOES (CHOPPED) 100 GRAM": 105.00,
        "PEPPER (BLENDED) 40 GRAM": 40.00,
        "CRAYFISH 10 GRAM": 70.00,
        "DRY FISH 20 GRAM": 200.00,
        "KNORR CUBE 4 GRAM": 44.00,
        "UGWU (PUMPKIN) 400 GRAM": 400.00,
        
    },

    "KIDNEY SAUCE": {
        "KIDNEY 250 GRAM": 1500.00,
        "ONIONS (CHOPPED) 30 GRAM": 30.00,
        "PEPPER (CHOPPED) 4 GRAM": 4.00,
        "KNORR CUBE 4 GRAM": 44.00,
        "VEGETABLE OIL 30 ML": 63.00,
        "CURRY 2 GRAM": 12.00,
        "THYME 2 GRAM": 12.00,
        "GREEN PEPPER 4 GRAM": 3.7,
        "YELLOW PEPPER 4 GRAM": 3.7,
        "RED PEPPER 4 GRAM": 3.7,
        "GARLIC 10 GRAM": 55.00,
        "CORN FLOUR 15 GRAM": 32.00,
        "SALT 0.5 GRAM": 0.25,
    },

    "EGG SAUCE": {
        "VEGETABLE OIL 30 ML": 63.00,
        "ONIONS 10 GRAM": 10.00,
        "PEPPER 4 GRAM": 3.7,
        "TOMATOES 10 GRAM": 30.00,
        "EGG 2 PCS": 300.00,
        "SALT 2.5 GRAM": 1.25,
        "TOMATOE PUREE 15 GRAM": 37.5,
        "KNORR CUBE 4 GRAM": 44.00,
        "SPRING ONIONS 15 GRAM": 45.00,
        "GREEN PEPPER/RED PEPPER 20 GRAM": 50.00,
    },

    "FISH SAUCE": {
        "OLIVE OIL 30 ML": 63.00,
        "Onions 30 GRAM": 30.00,
        "Garlic 2 GRAM": 11.00,
        "pepper 20 GRAM": 20.00,
        "Tomato 10 GRAM": 30.00,
        "knorr cube 4 GRAM": 44.00,
        "Salt 2.5 GRAM": 1.25,
        "CAT FISH (CUT 3) 433.33 GRAM": 1299.00,
        "Green bell pepper 4 GRAM": 3.7,
        "Yellow bell pepper 4 GRAM": 3.7,
        "Red bell pepper 4 GRAM": 3.7,
        "corn flour 15 GRAM": 32.00,
        "white/black pepper 1 gram": 42.00,
        
    },

    "BEEF SAUCE": {
        "BEEF (3 PCS) CUT 12 250 GRAM": 750.00,
        "Garlic 2 GRAM": 11.00,
        "Ginger 2 GRAM": 11.00,
        "knorr cube 4 GRAM": 44.00,
        "Salt 2.5 GRAM": 1.25,
        "Flour 7 GRAM": 9.5,
        "Vegetable oil 30 ML": 63.00,
        "Onion 10 GRAM": 10.00,
        "Green Pepper 20 GRAM": 20.00,
        "Soy sauce 4 ML": 19.7,
        "Corn Flour 15 GRAM": 32.00,
        "FRESH TOMATOE 30 GRAM": 11.00,
        "WHITE/BLACK PEPPER 1 gram": 42.00,
        "SWEET CHILLI 2 ML": 9.00,
        
    },

    "CHICKEN SAUCE": {
        "CHICKEN (CUT 4) 400 GRAM": 1200.00,
        "Onions 30 GRAM": 30.00,
        "knorr cube 4 GRAM": 44.00,
        "Vegetable oil 30 ML": 63.00,
        "Curry 2 GRAM": 12.00,
        "Thyme 2 GRAM": 12.00,
        "Green bell pepper 4 GRAM": 3.7,
        "Yellow bell pepper 4 GRAM": 3.7,
        "Red bell pepper 4 GRAM": 3.7,
       
    },

    "GREEK SALAD": {
        "SLICE LETTUCE 30 GRAM": 90.00,
        "SLICE FRESH TOMATOES 170 GRAM": 170.00,
        "OLIVE SEED 6 PCS": 270.00,
        "BLACK PEPPER 0.5 GRAM": 16.00,
        "OLIVE OIL 4 ML": 60.00,
        "LIME ORANGE 15 ML": 30.00,
        "SALT 0.5 GRAM": 1.00,
        "CUCUMBER 10 GRAM": 60.00,
        "DICED PARSLEY, GARLIC 2 GRAM": 12.00,
        "LIME ORANGE 10 ML": 20.00,
        "VENIGAR 5ML": 5.00,
        "BAMA 10 ML": 40.00,
        "FETTER CHEESE 40 GRAM": 1000.00,
        "VENIGAR 5 ML": 45.00,
        
    },

    "VEG. SALAD": {
        "LETTUCE 30 GRAM": 90.00,
        "FRESH TOMATOE 170 GRAM":170.00,
        "OLIVE OIL 1 ML": 15.00,
        "BLACK PEPPER 0.5 GRAM": 16.00,
        "SALT 0.5 GRAM": 1.00,
        "VINEGAR 5 ML": 45.00,
        "SUGAR 0.5 GRAM": 1.00,
        "BOILED EGG (OPTIONAL) 2 EGG": 300.00,
        "LIME ORANGE 10 ML": 20.00,
        "MAYONAISE 50 ML": 200.00,
        "GARLIC 0.5 GRAM": 25.00,
        "PERMISSAN CHEESE 1 GRAM": 55.00,
        "OLIVE SEED 6 PCS": 270.00,
        
    },

    "CEASAR SALAD": {
        "LETTUCE 30 GRAM": 180.00,
        "BREAD 15 GRAM": 60.00,
        "CHICKEN BREAST 100 GRAM": 300.00,
        "WHITE PEPPER 0.5 GRAM": 16.00,
        "BENNY SPICE 0.5 GRAM": 3.00,
        "LIME ORANGE 10 ML": 20.00,
        "MAYONNAISE 30 ML": 120.00,
        "GARLIC 0.5 GRAM": 25.00,
        "OLIVE OIL 4ML": 60.00,
        "SUGAR 0.5 GRAM": 2.00,
        "BLACK PEPPER 0.5 GRAM": 16.00,
        "PERMISSAN CHEESE 20 GRAM": 1100.00,
        "OLIVE SEED 6 PCS": 270.00,
       
    },

    "CHEF SALAD": {
        "Egg 1 PCS": 150.00,
        "Chicken 100 GRAM": 300.00,
        "Beef 100 GRAM": 400.00,
        "Cheese 4 GRAM": 220.00,
        "Lettuce 30 GRAM": 180.00,
        "Cucumber 5 GRAM": 75.00,
        "Tomatoes 100 GRAM": 100.00,
        "Carrots 30 GRAM": 90.00,
       
    },

    "CRISPAN SALAD": {
        "lettuce 250 gram": 500.00,
        "cabbage 30 gram": 75.00,
        "carrot 20 gram": 50.00,
        "cucumber 30 gram": 180.00,
        "mayonnaise 30 ml": 111.00,
        "sweet syrup 0.5 GRAM": 1.00,
        "salt 0.5 GRAM": 1.00,
        "venigar 5 ML": 45.00,
        "egg 2 pcs": 300.00,
        "chicken 400 grams": 1280.00,
        "sausage 1 pcs": 100.00,
        "baked beans 10 gram": 125.00,
        "fresh tomatoe 50 gram": 18.00,
       
    },

    "COLESLAW": {
        "cabbage 350 gram": 875.00,
        "carrot 50 gram": 125.00,
        "cream 30 ml": 196.00,
        "sweet syrup 2 gram": 3.4,
        "salt 0.5 gram": 1.00,
        "venigar 5 ML": 45.00,
        "egg 2 pcs": 300.00,
        "milk 4 ml": 26.00,
                
    },

    "RUSSIAN SALAD": {
        "carrot 30 gram": 75.00,
        "green pea 60 GRAM": 150.00,
        "irish potatoe 300 grams": 325.00,
        "chicken luncheon 30 grams": 220.00,
        "white/black pepper 1 gram": 42.00,
        "sweet syrup 2 gram": 3.40,
        "salt 0.5 gram": 0.25,
        "cream 30 gram": 196.00,
        "egg 2 pcs": 300.00,
       
    },

    "FULL STEAM VEG.": {
        "CABBAGE 100 GRAM": 250.00,
        "CARROT 30 gram": 75.00,
        "GREEN BEANS 50 GRAMS": 125.00,
        "BROCOLLI 40 gram": 100.00,
        "CAULI FLOWER 40 gram": 100.00,
        "SWEET CORN 30 GRAMS": 96.00,
        "MUSHROOM 30 GRAMS": 116.00,
        "SALT 0.5 gram": 1.00,
        "SESAME OIL 0.5 gram": 3.80,
        "WHITE PEPPER 0.5 gram": 20.8,
        "KNORR CUBE 0.5 gram": 5.30,
       
    },

    "SIDE STEAM VEG.": {
        "CABBAGE 100 GRAM": 250.00,
        "CARROT 30 GRAMS": 75.00,
        "GREEN BEANS 50 GRAMS": 125.00,
        "BROCOLLI 40 GRAMS": 100.00,
        "CAULI FLOWER 40 GRAMS": 100.00,
        "SWEET CORN 30 GRAMS": 96.00,
        "MUSHROOM 30 GRAMS": 116.00,
        "SALT 0.5 GRAM": 1.00,
        "SESAME OIL 0.5 GRAM": 3.8,
        "WHITE PEPPER 0.5 GRAM": 20.8,
        "KNORR CUBE 0.5 GRAM": 5.3,
       
    },

    "SIDE SALAD": {
        "CABBAGE 30 GRAM": 75.00,
        "LETTUCE 40 GRAM": 80.00,
        "FRESH TOMATOE 20 gram": 14.7,
        "CARROT 10 GRAMS": 25.00,
        "SALT 0.5 GRAM": 0.25,
        "SWEET SYRUP 2 gram": 3.4,
        "VENIGAR 5 ML": 45.00,
       
    },

    "SAUSAGE": {
        "SAUSAGE 3 PCS": 300.00,
        "OLIVE OIL 15 ML": 218.00,
        "SWEET CHILLI 2 ML": 9.00,
        "OYSTER SAUCE 2 ML": 8.00,
        "WHITE/BLACK PEPPER 1 gram": 45.00,
    },

    "BECON": {
        "BECON 200 GRAM": 1000.00,
        "OLIVE OIL 15 ML": 218.00,
        "SWEET CHILLI 2 ML": 9.00,
        "OYSTER SAUCE 2 ML": 8.00,
        "WHITE/BLACK PEPPER 1 gram": 42.00,
    },

    "HOT DOG": {
        "HOT DOG 4 PCS": 54.00,
        "SWEET CHILLI 2 ML": 9.00,
        "OYSTER SAUCE 2 ML": 8.00,
        "WHITE/BLACK PEPPER 1 gram": 42.00,
        "OLIVE OIL 15 ML": 218.00,
    },

    "POTATOE CHIPS": {
        "IRISH POTATOE 200 GRAM": 200.00,
        "SALT 2 GRAM": 2.00,
        "VEGETABLE OIL 30 ML": 60.00,
        "ONION 30 GRAM": 75.00,
    },

    "OAT": {
        "OAT 70 GRAM": 280.00,
        "SUGAR 15 GRAM": 30.00,
        "MILK 30 GRAM": 210.00,
       
    },

    "TOAST BREAD": {
        "BREAD 40 GRAM": 280.00,
        "JAM 20 GRAM": 100.00,
        "BUTTER 20 GRAM": 120.00,
        
    },

    "FRENCH TOAST": {
        "MILK 63 GRAM": 441.00,
        "EGG 1 PCS": 150.00,
        "SALT 4 GRAM": 4.00,
        "VANILLA EXTRACT 4 GRAM": 28.00,
        "BREAD 40 GRAM": 280.00,
        "OLIVE OIL 15 ML": 225.00,
        "CINNAMON 4 GRAM": 96.00,
       
    },

    "AMERICAN PANCAKE WITH LOCAL SCRAMBLE": {
        "FLOUR 142 GRAM": 142.00,
        "BAKING POWDER 4 GRAM": 12.00,
        "SUGAR 30 GRAM": 60.00,
        "SALT 2 GRAM": 2.00,
        "BUTTER 120 GRAM": 360.00,
        "EGG 4 PCS": 600.00,
        "VANILLA EXTRACT 2 GRAM": 14.00,
    },

    "CORN & CHICKEN SOUP": {
        "VEG. OIL 15 ML": 31.80,
        "FRESH GARLIC 4 GRAM": 0.22,
        "FRESH GINGER 2 GRAM": 0.11,
        "VINEGAR 2ML": 1.30,
        "BENNY SPICE 0.5 GRAM": 2.34,
        "SALT 0.5 GRAM": 0.38,
        "SWEET CORN 0.50 GRAM": 2.8,
        "FRESH CHICKEN 40 GRAM": 120.00,
        "CORN STARCH SYRUP 16ML": 33.00,
        "EGG 1 PCS": 150.00,
        "DARK SOY OIL 2ML": 8.8,
        "PARSLEY LEAF 0.50 GRAM": 2.5,
        "UNSORTED BUTTER 4 GRAM": 11,
        "BREAD ROLL 1 ROLL": 500,
    },

    "CHICKEN MINISTRONI SOUP": {
        "FRESH CHICKEN 40 GRAM": 120.00,
        "OLIVE OIL 5ML": 72.50,
        "FRESH GARLIC 0.5 GRAM": 0.55,
        "FRESH GINGER 0.5 GRAM": 0.55,
        "FRESH TOMATOES 40 GRAM": 42.00,
        "ONION 5 GRAM": 2.7,
        "SPAGHETTI 40 GRAM": 66.00,
        "TOMATOE PUREE 0.5 GRAM": 1.14,
        "WHITE PEPPER 0.5 gram": 20.8,
        "LECK 2 GRAM": 10.00,
        "CORN SYRUP 20 ML": 41.6,
        "VEGES 40 GRAM": 80.00,
        "KNORR CUBE 0.5 GRAM": 10.7,
        "PARSLEY 2 GRAM": 8.00,
        "IRISH, CARROT,CABBAGE 40 GRAM": 80.00,
        "SALT 0.5 GRAM": 0.38,
        "BREAD ROLL 1 PCS": 500.00,
        
    },

    "SWEET & SOUR CHICKEN": {
        "FLOUR 50 GRAM": 76.00,
        "CURRY POWDER 1 TBL SP (4 GRAM)": 22.00,
        "SALT 1 PINCH (1/8)": 0.38,
        "HOT CHILLI 1 PINCH (1/8)": 7.00,
        "STAR CUBE 1 PINCH (1/8)": 10.70,
        "BAKING POWDER 1 TSP (4 GRAM)": 13.9,
        "WHITE PEPPER 0.5 gram": 20.8,
        "DICED CHICKEN 400 GRAM": 1120.00,
        "KNORR CUBE 0.5 GRAM": 10.7,
        "OLIVE OIL 30 ML": 435.00,
        "KETCHUP 45 ML": 294,
        "VENIGAR 6ML": 3.9,
        "SUGAR 2 GRAM": 3.13,
        "WHITE PEPPER 1 GRAM": 41.6,
        "HOT CHILLI (OPTIONAL) 0.5 GRAM": 7.00,
        "KNORR CUBE 0.5 GRAM": 10.7,
        "BENNY SPICE 0.5 GRAM": 4.7,
        "CORN FLOUR 4ML": 8,
        "MIXED VEGES 100 GRAM": 300.00,
       
    },

    "BEEF STROGANOF": {
        "VEGETABLE OIL 45 ML": 95.4,
        "FRESH GARLIC 0.5 GRAM": 0.55,
        "DICED BEEF 250 GRAM": 850.00,
        "MUSHROOM 120 GRAM": 287.00,
        "CORN FLOUR 30 GRAM": 62.5,
        "OYSTER SAUCE V": 59,
        "SESAME OIL 5 ML": 37.5,
        "BLACK PEPPER 1 GRAM": 40.9,
        "WHITE PEPPER 0.5 gram": 20.8,
        "CORN FLOUR 4 GRAM": 8.00,
        "CASHEW NUT 4 PCS": 120,
        "DARK SOY OIL 5 ML": 22.00,
        "OREGANO 0.5 GRAM": 9.1,
        "KNORR CUBE 0.5 GRAM": 10.7,
        "RED WINE 10 ML": 106.7,
        
    },

    "GRILLED POTATOE": {
        "VEGETABLE OIL 30 ML": 63.6,
        "IRISH POTATOE 100 GRAM": 91.6,
        "PARSLEY FLAKES 0.5 GRAM": 9.1,
        "BROCOLLI 30 GRAM": 75.00,
        "COLEY FLOUR 40 GRAM": 120.00,
        "CARROT 40 GRAM": 120.00,
        "CABBAGE 40 GRAM": 120.00,
        
    },

    "CHICKEN IN HOT PLATE": {
        "OLIVE OIL 45 ML": 653.00,
        "FRESH GARLIC 0.5 GRAM": 0.55,
        "ONIONS 30 GRAM": 16,
        "DICE CHICKEN 400 GRAM": 1120.00,
        "TOMATOE SAUCE 60 ML": 137.5,
        "KNORR CUBE 0.5 GRAM": 10.7,
        "SESAME OIL 2ML": 15.00,
        "OYSTER SAUCE 2ML": 7.8,
        "MIXED VEGES 150 GRAM": 375.00,
        "WHITE WINE 5 ML": 533.00,
        
    },

    "SNOW BASMATIC RICE": {
        "PLAIN BASMATIC RICE 180 GRAM": 666.00,
        "VEGES 100 GRAM": 250.00,
        
    },

    "MUSHROOM SOUP": {
        "Butter 30 GRAM": 166.00,
        "Benny spice 0.5 GRAM": 1.6,
        "Onions 30 GRAM ": 26.00,
        "Garlic 2 GRAM": 2.00,
        "Mushroom 100 GRAM": 400.00,
        "corn flour 15 GRAM": 15.00,
        "white Pepper 0.5 gram": 20.8,
        "cream 50 GRAM": 326.00,
        "Salt ": 75.00,
        "Salt 0.5 GRAM": 0.25,
        "Parsley 2 GRAM": 40.00,
        
    },

    "CREAM OF TOMATOE SOUP": {
        "OLIVE OIL 30 ML": 435.00,
        "Onions 20 GRAM": 17.3,
        "Garlic 4 GRAM": 22.00,
        "benny spice 0.5 GRAM": 1.6,
        "Tomatoe 30 gram": 11.00,
        "Salt 0.5 GRAM": 0.25,
        "Sweet syrup (sugar) 4 GRAM": 6.8,
        "white Pepper 0.5 gram": 20.8,
        "Cream 15 GRAM": 97.8,
        "corn flour 15 GRAM": 31.2,
        
    },

    "CREAM OF CARROT SOUP": {
        "OLIVE OIL 30 ML": 435.00,
        "Onions 20 GRAM": 17.3,
        "Garlic 4 GRAM": 22.00,
        "benny spice 0.5 GRAM": 1.6,
        "carrot 30 gram": 11.00,
        "Salt 0.5 GRAM": 0.25,
        "Sweet syrup (sugar) 4 GRAM": 6.8,
        "white Pepper 0.5 gram": 20.8,
        "Cream 15 GRAM": 97.8,
        "corn flour 15 GRAM": 31.2,
       
    },

    "CREAM OF ONION SOUP": {
        "Onions 60 GRAM": 52.00,
        "Salt 0.5 GRAM": 0.25,
        "corn flour 15 GRAM": 31.2,
        "Cream 15 GRAM": 97.8,
        "Permessan Cheese 5 GRAM": 275.00,
        "Lemon 4 ML": 20.00,
        "olive oil 15 ML": 217.5,
        "cream 15 GRAM": 97.8,
        "white pepper 0.5 gram": 20.8,
        "garlic 4 GRAM": 22.00,
        "sugar 15 GRAM": 25.5,
        "benny spice 0.5 GRAM": 1.6,
        
    },

    "BEEF GOULASH": {
        "BEEF 250 GRAM": 1050.00,
        "olive oil 30 ML": 435.00,
        "Onions 15 GRAM": 13.00,
        "Garlic 2 GRAM": 0.11,
        "Paprika 2 GRAM": 100.00,
        "Tomatoes 100 GRAM": 367.00,
        "tomatoes paste 30 GRAM": 75.00,
        "white pepper 0.5 gram": 20.8,
        "Mushroom 43.75 GRAM": 165.00,
        "Corn Flour 15 GRAM": 32.00,
        "red wine (veleta) 5 ML": 533.00,
        "irish potatoe 20 gram": 21.6,
        "button onions 15 GRAM": 13.00,
        "jumbo carrot 10 gram": 3.67,
        
    },

    "CHICKEN CASSEROLE": {
        "Chicken 400 GRAM": 1280.00,
        "Cream 60 GRAM": 128.00,
        "Onion 60 GRAM": 52.00,
        "Mushrooms 125 GRAM": 482.00,
        "salt 0.5 GRAM": 0.25,
        "olive oil 30 ML": 217.5,
        "garlic 10 GRAM": 55.00,
        "tomatoes 4 GRAM": 1.4,
        "tomatoe paste 4GRAM": 10.00,
        "white pepper 0.5 gram": 20.8,
        "carrot and green beans 3 gram": 7.5,
        "boiled egg(optional) 1 pcs": 150.00,
        "irish potatoe 5 gram": 5.4,
        
    },

    "MIXED GRILL": {
        "beef stake 40 gram": 168.00,
        "fish fillet 50 gram": 160.00,
        "chicken breast 50 gram": 160.00,
        "liver 40 gram": 120.00,
        "sausage 1 pcs": 100.00,
        "sunny side up 1 pcs": 150.00,
        "red wine 5 ML": 533.00,
        "steam veg. brocolli, carrot 10 GRAM": 25.00,
        "white pepper 0.5 gram": 20.8,
        "corn flour 15 GRAM": 31.2,
        "dark sauce 2 ML": 8.8,
        "knorr cube 0.5 gram": 5.3,
        "fresh tomatoes 2 gram": 0.7,
        "onions 15 GRAM": 13.00,
        "garlic 4 GRAM": 22.00,
        
    },

    "GOUJONS OF FISH": {
        "FISH (CUT 3) 433 GRAM": 1385.00,
        "Egg 1 PCS": 150.00,
        "Breadcrumbs ": 0.00,
        "Salt 0.5 GRAM": 0.25,
        "white pepper 0.5 gram": 20.8,
        "Flour 2 GRAM": 2.7,
        "Vegetable oil 15 ML": 31.8,
        "benny seed 50 gram": 250.00,
        "mayonnaise 80 ml": 294.00,
        "salt 0.5 GRAM": 0.25,
        "boiled egg 1 pcs": 150.00,
        "sugar 0.5 GRAM": 0.85,
        "parsley 10 gram": 40.00,
        "cellery 10 gram": 40.00,
        
    },

    "CHICKEN ESCALOPE": {
        "CHICKEN BREAST 400 GRAM": 1120.00,
        "KNORR CUBE 0.5 GRAM": 10.7,
        "SALT 0.5 GRAM": 0.38,
        "WHITE PEPPER 0.5 gram": 20.8,
        "EGG 1 PCS": 150.00,
        "VEGETABLE OIL (FOR FRYING) 500 ML": 0.00,
        
    },

    "SHRIMPS IN HOT PLATE": {
        "Shrimps 250 GRAM": 2950.00,
        "Ginger 6 GRAM": 33.00,
        "Garlic 6 SLICES": 33.00,
        "Celery 2 GRAM": 40.00,
        "Onions 30 GRAM": 26.00,
        "Red Pepper 4 GRAM": 3.7,
        "Green Pepper 4 GRAM": 3.7,
        "Sesame oil 4 ML": 31.00,
        "Soy sauce 4 ML": 19.7,
        "Oyster 1 TSP": 15.7,
        "salt 4 GRAM": 2.00,
        "cornstarch 150 GRAM": 321.00,
        "white wine 5 ML": 533.00,
        "veges 100 gram": 166.00,
        "sweet corn 20 gram": 63.00,
        
    },

    "FISH IN HOT PLATE": {
        "FISH (CUT 3) 433 GRAM": 1385.00,
        "Ginger 6 GRAM": 33.00,
        "Garlic 6 SLICES": 33.00,
        "Celery 2 GRAM": 40.00,
        "Onions 30 GRAM": 26.00,
        "Red Pepper 4 GRAM": 3.7,
        "Green Pepper 4 GRAM": 3.7,
        "Sesame oil 4 ML": 31.00,
        "Soy sauce 4 ML": 19.7,
        "Oyster 1 TSP": 15.7,
        "salt 4 GRAM": 2.00,
        "wine 15 ml": 1599.00,
        "cornstarch 15 GRAM": 32.00,
        
    },

    "CHICKEN GORDON BLUI": {
        "CHICKEN BREAST 400 GRAM": 1120.00,
        "KNORR CUBE 0.5 gram": 10.7,
        "SALT 0.5 gram": 0.38,
        "WHITE PEPPER 0.5 gram": 20.8,
        "HAM 4 SLICED": 35.2,
        "MOZOROLLA CHEESE 50 GRAM": 76.00,
        "EGG 1 PCS": 141.6,
        "VEGETABLE OIL (FOR FRYING) 500 ML": 0.00,
        "WHITE FLOUR 30 GRAM": 40.8,
        "OLIVE OIL 15 ML": 217.00,
        "ONIONS 15 GRAM": 8.00,
        "GARLIC 0.5 gram": 0.55,
        "CORN FLOUR 15 ML": 22.8,
        "OYSTER SAUCE 15 ML": 59.2,
        "BLACK PEPPER 0.5 gram": 41.6,
        "WHITE PEPPER 0.5 gram": 41.6,
        "HOT CHILLI 0.5 gram": 7.00,
        "DARK SOY OIL 5 ml": 22.00,
        "SEASONING CUBE 0.5 gram": 10.7,
        "RED WINE 8 ML": 1.07,
        
    },

    "FISH FILLIT": {
        "VEG. OIL 75 ML": 159.00,
        "FRESH GARLIC 0.5 gram": 0.55,
        "FISH (CAT FISH) 433.33 GRAM": 1300.00,
        "PEPPER SAUCE 30 ML": 103.00,
        "CORN FLOUR 15 ML": 31.00,
        "OYSTER SAUCE 5 ML": 19.6,
        "KNORR CUBE 0.5 gram": 10.7,
        "GREEN BEANS/CARROT/BROCOLLI 100 GRAM": 250.00,
        "ONIONS 30 GRAM": 16.00,
        "KNORR CUBE 0.5 gram": 10.7,
        "hot chilli 30 ML": 103.00,
        "FRESH GARLIC 0.5 gram": 0.55,
        "GREEN PEPPER 2 GRAM": 8.7,
        "dark sauce 2 ML": 8.8,
        "white wine 4 ML": 426.00,
        
    },

    "HALF BARBEQUE GRILL CHICKEN": {
        "CHICKEN 800 GRAM": 2300.00,
        "TOMATOE PUREE 215 GRAM": 493.00,
        "PEPPER SAUCE 10 ML": 34.4,
        "BARBEQUE SAUCE 15 ML": 67.00,
        "OREGANO 0.5 gram": 9.00,
        "FRESH GARLIC 0.5 gram": 0.27,
        "FRESH GINGER 4 GRAM": 0.22,
        "KNORR CUBE 1 CUBE": 10.7,
        "VEG. OIL 15 ML": 31.8,
        "ONION 2  gram": 0.53,
        "CUCUMBER 10 GRAM": 15.00,
        "FRIED IRISH 100 GRAM": 91.6,
        "FRESH TOMATOE 1 PCS": 1.5,
        "HOT CHILLI SAUCE 50 GRAM": 347.00,
        "SEASONING (KNORR) 0.5 gram": 26.00,
        
    },

    "GRILL WHOLE CHICKEN": {
        "Ginger 30 GRAM": 165.00,
        "Garlic 30 GRAM": 165.00,
        "Onion 30 GRAM": 26.00,
        "Pepper 4 GRAM": 3.7,
        "Parsley 2 GRAM": 40.00,
        "Salt 4 GRAM": 2.00,
        "lemon 50 ML": 500.00,
        "olive oil 60 ML": 870.00,
        "Star cube 8 GRAM": 85.00,
        "Fresh Tomato 10 GRAM": 3.7,
        "Tomato paste 45 gram": 112.5,
        "Shombo 4 GRAM": 3.7,
        "Chicken 2000 gram": 9200.00,
        
    },

    "CHICKEN WINGS": {
        "Ginger 30 GRAM": 165.00,
        "Garlic 30 GRAM": 165.00,
        "Onion 30 GRAM": 26.00,
        "Pepper 4 GRAM": 3.7,
        "Parsley 2 GRAM": 40.00,
        "salt 4 GRAM": 4.00,
        "lemon 20 ML": 200.00,
        "knorr cube 8 GRAM": 86.00,
        "Fresh Tomato 10 GRAM": 3.7,
        "Tomato paste 30 gram": 75.00,
        "Shombo 4 GRAM": 3.7,
        "Chicken 300 GRAM": 1380.00,
        "olive oil 60 ML": 870.00,
        
    },

    "MIXED MEAT FRIED RICE": {
        "OLIVE OIL 30 ML": 435.00,
        "CHICKEN 100 GRAM": 280.00,
        "ONIONS 20 GRAM": 10.7,
        "GARLIC 5 GRAM": 27.00,
        "EGG 1 PCS": 150.00,
        "BASMATIC RICE 180 GRAM": 666.00,
        "WHITE PEPPER 0.5 gram": 20.80,
        "OYSTER SAUCE 5 ML": 19.6,
        "SESAME OIL 5 ML": 37.5,
        "DARK SOY OIL 5 ML": 22.00,
        "KNORR CUBE 0.5 GRAM": 10.7,
        "MIXED VEGES 100 GRAM": 150.00,
        "FRESH PEPPER 0.5 GRAM": 3.5,
        "OLIVE OIL 30 ML": 435.00,
        "BEEF 80 GRAM": 272.00,
        "BENNY SPICE 0.5 GRAM": 4.7,
        "PEPPER SAUCE 2 GRAM": 6.7,
        "CORN FLOUR 15 ML": 31.00,
        "OYSTER SAUCE 2 ML": 7.8,
        "WHITE PEPPER 0.5 gram": 20.8,
        "GREEN PEPPER 10 GRAM": 43.00,
        "FRESH PEPPER 0.5 GRAM": 3.5,
        "shrimps 20 grams": 236.00,
    },

    "MEXICAN FRIED RICE": {
        "Olive oil 30 ml": 435.00,
        "Onions 30 GRAM": 26.00,
        "Tomatoes 200 GRAM": 73.4,
        "Sweet Corn 20 GRAM": 63.7,
        "Green Chiles 10 GRAM": 13.00,
        "knorr cube 4 GRAM": 43.00,
        "Garlic 2 GRAM": 11.00,
        "BASMATIC RICE 180 GRAM": 666.00,
        "diced sausage/beef 30 gram": 126.00,
        "sesame oil 4 ML": 31.00,
        "shreded carrot 40 gram": 14.5,
        "carrot 20 gram": 7.3,
        "green beans 10 GRAM": 25.00,
        "salt 0.5 GRAM": 0.25,
        
    },

    "CHINESE FRIED RICE": {
        "Basmatic Rice 180 GRAM": 724.00,
        "Salt 0.5 GRAM": 0.25,
        "Butter 15 GRAM": 83.00,
        "olive oil 15 ML": 218.00,
        "Onions 30 GRAM": 26.00,
        "green Peas 30 GRAM": 250.00,
        "Carrots 10 GRAM": 3.7,
        "Ginger (optional) 15 gram": 82.5,
        "Garlic 5 GRAM": 27.5,
        "Egg 1 PCS": 150.00,
        "Soy sauce 15 ML": 46.00,
        "Sesame oil 15 ML": 116.00,
        "sweet corn 20 gram": 63.7,
        
    },

    "VEGETABLE FRIED RICE": {
        "olive oil 15 ML": 435.00,
        "Eggs 2 PCS": 300.00,
        "Garlic (15 GRAM)": 82.00,
        "Carrots 20 GRAM": 7.3,
        "Peas 100 GRAM": 250.00,
        "Cabbage 30 GRAM": 50.00,
        "Broccoli 20 GRAM": 50.00,
        "Cauliflower 20 GRAM": 50.00,
        "Sweetcorn 20 GRAM": 159.00,
        "basmatic Rice 180 GRAM": 724.00,
        "Soy sauce 15 ML": 46.00,
        "white pepper 0.5 gram": 20.8,
        "mushroom 20 gram": 77.00,
        "knorr cube 0.5 gram": 5.3,
        "bell pepper (red/green) 30 GRAM": 75.00,
        
    },

    "LEBANESE FRIED RICE": {
        "Lentils 20 GRAM": 200.00,
        "Onion 20 GRAM": 26.00,
        "Olive oil 30 ML": 435.00,
        "Vinegar 15 ML": 12.00,
        "Garlic 10 GRAM": 55.00,
        "Basmatic Rice 180 GRAM": 724.00,
        "cumning 0.5 gram": 22.8,
        "tumeric 10 gram": 30.00,
        "knorr cube 0.5 gram": 5.3,
        "white/black pepper 1 gram": 42.00,
        "cinnamon 0.5 gram": 17.8,
        "salt 0.5 GRAM": 0.25,
        
    },

    "ITALIAN FRIED RICE": {
        "Onions 30 GRAM": 26.00,
        "Garlic 15 GRAM": 82.00,
        "Ginger 15 GRAM": 82.00,
        "Red, Yellow and Green bell pepper 15 GRAM": 14.00,
        "Olive oil 30 ML": 435.00,
        "Basmatic Rice 180 GRAM": 724.00,
        "Salt 0.5 GRAM": 0.25,
        "white pepper 0.5 gram": 20.8,
        "corn beef 20 gram": 176.00,
        "mushroom 10 gram": 39.00,
        "diced liver/beef 20 gram": 60.00,
        "egg 1 pcs": 150.00,
        "knorr cube 0.5 gram": 5.3,
        "sesame oil 15 ML": 116.00,
        "carrot 20 GRAM": 7.3,
    },

    "STIRFRY B/FRIED RICE": {
        "olive oil 30 ML": 435.00,
        "Carrot 20 GRAM": 7.3,
        "Green Peas 20 GRAM": 250,
        "Sweetcorn 10 GRAM": 31.8,
        "Soy sauce 15 ML": 46.00,
        "Basmatic Rice 180 GRAM": 724.00,
        "garlic 10 GRAM": 55.00,
        "ginger 10 GRAM": 55.00,
        "brocolli 15 GRAM": 37.5,
        "cauli flower 15 GRAM": 37.5,
        "onions 20 GRAM": 26.00,
        "green peper 15 GRAM": 38.00,
        "red pepper 5 gram": 13.00,
        
    },

    "CURRY FRIED RICE": {
        "olive oil 15 ML": 218.00,
        "Onions 15 GRAM": 13.00,
        "Garlic 15 GRAM": 82.00,
        "Carrot 10 GRAM": 3.8,
        "Green pea 100 GRAM": 250.00,
        "Basmatic Rice 180 GRAM": 724.00,
        "Salt 0.5 GRAM": 0.25,
        "Soy sauce 15 ML": 46.00,
        "Curry Powder 15 GRAM": 89.00,
        
    },

    "PILAF RICE": {
        "Rice 180 GRAM": 724.00,
        "Butter 15 GRAM": 83.00,
        "Onions 20 GRAM": 17.3,
        "Garlic 10 GRAM": 82.00,
        "Salt 0.5 GRAM": 0.25,
        "olive oil 30 ML": 436.00,
        "groundnut 15 gram": 38.00,
        "thyme 0.5 GRAM": 4.00,
        "knorr cube 0.5 gram": 5.3,
        "white pepper 0.5 gram": 20.8,
        
    },

    "ENGLISH FRIED RICE": {
        "olive oil 30 ML": 436.00,
        "Onions 20 GRAM": 17.3,
        "Carrots 15 GRAM": 5.5,
        "green beans 20 GRAM": 50.00,
        "Garlic 10 GRAM": 55.00,
        "Rice 180 GRAM": 324.00,
        "Soy sauce 15 ML": 74.00,
        "Sesame Oil 1 ml": 7.8,
        "Salt 0.5 GRAM": 0.25,
        "white Pepper 0.5 gram": 20.8,
        "diced beef 40 gram": 168.00,
        "chicken luncheon 20 gram": 147.00,
        "sweet corn 20 gram": 63.7,
        "thyme 0.5 GRAM": 3.00,
        "egg 1 pcs ": 150.00,
    },

    "PASTA CARBONARA ": {
        "MUSHROOM 110 gram": 424.00,
        "OLIVE OIL 30 ML": 435.00,
        "FRESH GARLIC 0.5 gram": 0.55,
        "ONIONS 15 GRAM": 8.00,
        "FRESH EGG 1 PCS": 150.00,
        "SPAGHETTI 125 GRAM": 206.00,
        "COOKING CREAM (MILK) 30 ML": 62.5,
        "BENNY SPICE 0.5 gram": 4.7,
        "WHITE PEPPER 0.5 gram": 41.6,
        "EGG YORK 1 PCS": 150.00,
        "PARSLEY FLAKES 0.5 gram": 9.1,
        "BASIL LEAF 5 GRAM": 10.00,
        "BECON 40 gram": 180.00,
        "permessan cheese 15 gram": 825.00,
    },

    "PLAIN PASTA": {
        "Spaghetti 125 GRAM": 268.8,
        "Carrot 10 GRAM": 3.33,
        "Green Beans 10 GRAM": 13.00,
        
    },

    "PASTA ALFREDO": {
        "Spaghetti 125 G": 269.00,
        "olive oil 30 ML": 435.00,
        "Garlic 10 GRAM": 55.00,
        "Cream 15 GRAM": 97.8,
        "Parmesan Cheese 15 gram": 835.00,
        "Salt 0.5 gram": 0.25,
        "WHITE pepper 0.5 GRAM": 20.8,
        "BASIL 5 GRAM": 10.00,
        "CHICKEN BREAST 180 GRAM": 576.00,
        "MUSHROOM 20 gram": 77.00,
        "KNORR CUBE 0.5 gram": 5.3,
        "ONIONS 10 GRAM": 13.00,
        
    },

    "SPAGHETTI BOLOGNAISE": {
        "Beef 100 GRAM": 420.00,
        "Onion 30 GRAM": 26.00,
        "Garlic 15 GRAM": 82.00,
        "Tomatoes 30 GRAM": 11.00,
        "Tomato paste 15 gram": 38.00,
        "Red wine 15 ml": 1600.00,
        "spaghetti 125 GRAM": 268.8,
        "white/black pepper 1 gram": 42.00,
        "corn flour 4 gram": 9.00,
        "olive oil 30 ML": 435.00,
        "veges 30 GRAM": 75.00,
        "salt 0.5 GRAM": 0.55,
        
    },

    "PENNE ARABBIATTA": {
        "olive oil 15 ML": 218.00,
        "Garlic 10 GRAM": 55.00,
        "onions 15 gram": 13.00,
        "parsley Flakes 2 gram": 83.00,
        "Tomato 200 GRAM": 73.40,
        "Salt 0.5 GRAM": 0.25,
        "white Pepper 0.5 gram": 20.8,
        "spaghetti 125 GRAM": 268.8,
        "knorr cube 0.5 gram": 5.3,
        "plump tomatoes 200 GRAM": 73.00,
        "ketchup 15 gram": 45.00,
        "veges 30 GRAM": 75.00,
        
    },

    "SINGAPOREAN NOODLES": {
        "Soy sauce 15 ML": 46.00,
        "Cooking wine 10 ml": 1066.00,
        "Curry Powder 2 GRAM": 118.00,
        "white Pepper 0.5 gram": 20.8,
        "Rice stick 50 GRAM": 625.00,
        "olive oil 30 ML": 435.00,
        "Shrimp/Prawns 50 GRAM": 590.00,
        "Egg 1 PCS": 150.00,
        "Garlic 10 GRAM": 82.00,
        "Ginger 20 GRAM": 82.00,
        "Onion 20 GRAM": 26.00,
        "DICED BEEF 40gram": 168.00,
        "CHICKEN 40 Gram": 128.00,
        "thyme 0.5 gram": 5.00,
        "salt 0.5 GRAM": 1.00,
       
    },

    "SPAGHETTI WITH INDIAN BEEF BALL": {
        "Onions 20 GRAM": 26.00,
        "Garlic 10 GRAM": 82.00,
        "olive oil 30 ML": 435.00,
        "Parsley 2 gram": 83.00,
        "Parmesan Cheese 10 GRAM": 550.00,
        "Egg 1 PCS": 150.00,
        "salt 0.5 GRAM": 0.25,
        "WHITE pepper 0.5 gram": 20.8,
        "Oregano 0.5 gram": 20.8,
        "Tomato 30 GRAM": 11.00,
        "Tomato PASTE 4 gram": 10.00,
        "Meatballs 100 GRAM": 420.00,
        "Spaghetti 125 GRAM": 268.8,
        "Basil PINCH": 40.00,
        "MINCED MEAT 150 GRAM": 698.00,
        "WHITE FLOUR 30 GRAM": 40.8,
    },
    "VEGETABLE NOODLES": {
        "OLIVE OIL 30 ML": 435.00,
        "Ginger 10 GRAM": 82.00,
        "Garlic 10 GRAM": 82.00,
        "Onions 15 GRAM": 26.00,
        "Green bell pepper 10 GRAM": 9.3,
        "Red bell pepper 10 GRAM": 9.3,
        "yellow bell pepper 10 GRAM": 9.3,
        "Carrot 10 GRAM": 4.00,
        "Spring Onions 10 GRAM": 15.00,
        "KNORR CUBE 0.5 gram": 5.3,
        "Soy sauce 5 ml": 25.00,
        "Salt 0.5 GRAM": 0.25,
        "Cabbage 10 Gram": 25.00,
        "NOODLES 250 GRAM": 350.00,
    },"STIRFRY PASTA": {
        "Spaghetti 125 GRAM": 268.8,
        "OLIVE OIL 30 ML": 435.00,
        "Garlic 10 GRAM": 55.00,
        "Onions 15 GRAM": 13.00,
        "Carrots 20 gram": 5.00,
        "PARSLEY Flakes 2 gram": 83.00,
        "Salt 0.5 GRAM": 2.00,
        "Soy sauce 15 ML": 46.00,
        "BROCOLLI 15 GRAM": 37.5,
        "CAULI FLOWER 15 GRAM": 37.5,
        "SESAME OIL 5 ML": 39.00,
        "GREEN BEANS 10 GRAM": 13.00,
        
    },
    "FRIED NOODLES": {
        "NOODLES 250 GRAM": 350.00,
        "OLIVE OIL 30 ML": 435.00,
        "Pepper 10 GRAM": 9.3,
        "Carrots 10 GRAM": 4.00,
        "Green peas 10 GRAM": 26.00,
        "KNORR CUBE 0.5 gram": 5.3,
        "GARLIC 10 GRAM": 55.00,
        "SESAME OIL 5 ML": 39.00,

    },"PASTA JOLLOF": {
        "SPAGHETTI 125 GRAM": 206.25,
        "VEGETABLE OIL 45 ML": 95.4,
        "CURRY 2 GRAM": 11.06,
        "KNORR CUBE 2 GRAM": 21.5,
        "ONIONS 20 GRAMS": 11.00,
        "THYME 0.5 gram": 5.5,
        "TOMATOE PASTE  45 GRAM": 103.00,
        "CARROT 20 GRAM": 14.00,
        "GREEN BEANS 30 GRAMS": 130.00,
        
    },

    "CROSSANT": {
        "FLOUR 70 GRAM": 106.40,
        "BUTTER (UNSALTED) 20 GRAM": 66.7,
        "SUGAR 4 GRAM": 6.24,
        "EGG 1 PCS": 0.1,
        "MILK 8 GRAM": 54.4,
        "YEAST 1.5 GRAM": 7.5,
        "MINCED MEAT 50 GRAM": 170.00,
        
    
    },"MEAT PIE": {
        "IRISH POTATOE 62.5 GRAM": 57.3,
        "CARROT 12.5 GRAM": 8.8,
        "VEGETABLE OIL 4 ML": 8.5,
        "ONIONS 2.5 GRAM": 1.34,
        "GINGER & GARLIC (BLENDED) 1.3 GRAM": 0.14,
        "KNORR CUBE 0.69 GRAM": 18.00,
        "CURRY 1 GRAM": 5.5,
        "THYME 0.25 GRAM": 1.38,
        "HOT PEPPER 0.25 GRAM": 1.7,
        "SALT 0.5 gram": 0.38,
        "FLOUR 62.5 GRAM": 95.00,
        "BUTTER 31.3 GRAM": 104.00,
        "MINCED MEAT 31.3 GRAM": 106.00,
    },
    "CHICKEN PIE": {
        "CHICKEN 62.5 GRAM": 187.5,
        "SALT 0.5 gram": 0.38,
        "KNORR 0.19 GRAM": 5.00,
        "CURRY 0.25 GRAM": 1.4,
        "GINGER & GARLIC 1.25 GRAM": 0.13,
        "HOT PEPPER 0.25 GRAM": 1.7,
        "FLOUR 62.5 GRAM": 95.00,
        "KNORR CUBE 0.5 GRAM": 13.00,
        "BUTTER 31.3 GRAM": 104.00,
        "IRISH POTATOE 62.5 GRAM": 57.3,
        "VEGETABLE OIL 5 ML": 10.6,
        "CARROTS 12.5 GRAM": 8.8,
        "ONIONS 2.5 GRAM": 1.34,
        "GINGER & GARLIC 1.25 GRAM": 0.13,
        "HOT PEPPER 0.25 GRAM": 1.7,
       
    },
    
    "CHICKEN PIZZA": {
        "CHICKEN 150 GRAMS": 450.00,
        "FLOUR 200 GRAMS": 304.00,
        "GARLIC 2 PINCH": 0.11,
        "KNORR CUBE 4 gram": 26.00,
        "WHITE PEPPER 0.5 gram": 41.00,
        "SUGAR 40 GRAM": 42.4,
        "SALT 1.5 TSP": 0.56,
        "ONION 5 GRAM": 2.7,
        "YEAST 7 GRAM": 35.00,
        "VEGETABLE OIL 60 ML": 127.2,
        "GARLIC 0.5 gram": 0.55,
        "MILK 250 GRAM": 1700.00,
        "MOZOROLLA CHEESE 120 GRAM": 720.00,
        "TOMATOE 200 GRAM": 210.00,
        "KNORR CUBE 0.5 gram": 26.00,
        "SALT 0.5 gram": 0.38,
        "KETCHUP 30 ML": 196.00,
        "TOMATOE SAUCE 50 GRAM": 115.00,
        
    },
    
    "VEGETABLE PIZZA": {
        "FLOUR 200 GRAMS": 304.00,
        "GARLIC 2 PINCH": 0.11,
        "KNORR CUBE 1 PCS": 26.00,
        "WHITE PEPPER 0.5 gram": 41.00,
        "SUGAR 40 GRAM": 62.4,
        "SALT 1.5 gram": 0.56,
        "ONION 5 GRAM": 2.7,
        "YEAST 15 GRAM": 75.00,
        "SALT 1.5 gram": 0.58,
        "VEGETABLE OIL 60 ML": 127.2,
        "GARLIC 0.5 gram": 0.55,
        "MILK 250 GRAM": 1700.00,
        "SALT 0.5 gram": 0.38,
        "MUSHROOM 30 GRAM": 72.00,
        "FRESH TOMATOE 40 GRAM": 42.00,
        "KNORR CUBE 0.5 gram": 26.00,
        "SALT 0.5 gram": 0.38,
        "KETCHUP 30 ML": 196.00,
        "TOMATOE SAUCE 50 GRAM": 115.00,
    },
    
    "FISH PIE": {
        "FISH 62.5 GRAM": 200.00,
        "ONIONS 0.8 GRAM": 0.43,
        "KNORR MAGGI 0.5 GRAM": 13.00,
        "GARLIC 0.5 gram": 0.55,
        "CURRY 0.5 GRAM": 2.8,
        "PEPPER 0.5 GRAM": 3.5,
        "IRISH POTATOE 62.5 GRAM": 57.3,
        "CARROT 12.5 GRAM": 8.8,
        "FLOUR 62.5 GRAM": 950.00,
        "KNORR MAGGI 2 GRAM": 52.00,
        "BUTTER 31.3 GRAM": 104.00,
    },
    
    "BEEF BURGER": {
        "FLOUR 120 GRAM": 182.4,
        "SUGAR 50 GRAM": 78.00,
        "BUTTER 50 GRAM": 167.00,
        "SALT 15 GRAM": 5.6,
        "MILK 20 GRAM": 136.00,
        "MINCED MEAT 80 GRAM": 272.00,
        "KETCHUP 30ML": 195.00,
        "BAMA 30 ml": 111.00,
        "CHEESE 5 gram": 24.00,
        "LETTUCE 20 GRAM": 60.00,
        "CUCUMBER 30 GRAM": 45.00,
        "FRESH TOMATOES 50 GRAM": 115.00,
        
    },
    
    "CHICKEN BURGER": {
        "FLOUR 120 GRAM": 182.40,
        "SUGAR 50 GRAM": 78.00,
        "BUTTER 50 GRAM": 167.00,
        "SALT 15 GRAM": 5.6,
        "MILK 20 GRAM": 136.00,
        "CHICKEN 100 GRAM": 300.00,
        "KETCHUP 30ML": 195.00,
        "BAMA 2 TBL SPOON": 111.00,
        "CHEESE 5 gram": 24.00,
        "LETTUCE 20 GRAM": 60.00,
        "CUCUMBER 30 GRAM": 45.00,
        "FRESH TOMATOES 50 GRAM": 115.00,
    },

    "VANILLA CAKE": {
        "FLOUR 500 GRAM": 760.00,
        "SUGAR 200 GRAM": 312.00,
        "BUTTER 500 GRAM": 1667.00,
        "BAKING POWDER 2 GRAM": 7.00,
        "EGG 8 PCS": 1133.3,
        "VANILLA FLAVOUR 8 GRAM": 56.00,
        "MILK POWDER 20 GRAM": 136.00,
        "MILK FLAVOUR 4 GRAM": 28.00,
        
    },

    "CLUB SANDWICH": {
        "BREAD (FLOUR) 50 GRAM": 78.00,
        "CHICKEN BREAST 80 GRAM": 240.00,
        "LUNCHEON 50 GRAM": 441.00,
        "OLIVE OIL 218": 100.00,
        "BENNY SPICE 0.5 gram": 4.7,
        "MAYONNAISE 95 GRAM": 352.00,
        "KETCHUP 10 GRAM": 65.00,
        "SUGAR 4 GRAM": 6.00,
        "FRESH TOMATOE 5 gram": 2.3,
        "SAUSAGE 1PCS": 100.00,
        "CABBAGE 10 GRAM": 50.00,
        "LETTUCE 10 GRAM": 30.00,
        "CARROT 10 GRAM": 7.00,
        "BOIL EGG 1 PCS": 150.00,
        "SLICED CHEESE 10 GRAM": 240.00,
        "FRIED IRISH POTATOE 100 GRAM": 91.6,
        "KETCHUP 4 ML": 26.00,
        "TOMATOE 5 gram": 2.3,
        "Dressing": 75.00,    },

    "VEGETABLE SANDWICH": {
        "BREAD 50 GRAM": 76.00,
        "LUNCHEON 50 GRAM": 441.00,
        "OLIVE OIL 15 ML": 218.00,
        "BENNY SPICE 0.5 gram": 4.7,
        "SWEET CHILLI SAUCE 2 ml": 00.00,
        "MAYONNAISE 95 GRAM": 352.00,
        "KETCHUP 10 GRAM": 65.00,
        "SUGAR 4 GRAM": 6.00,
        "FRESH TOMATOE 5 gram": 2.3,
        "SAUSAGE 1PCS": 100.00,
        "CABBAGE 10 GRAM": 50.00,
        "LETTUCE 10 GRAM": 30.00,
        "CARROT 10 GRAM": 7.00,
        "BOIL EGG 1 PCS": 150.00,
        "SLICED CHEESE 10 GRAM": 240.00,
        "FRIED IRISH POTATOE 100 GRAM": 91.6,
        "KETCHUP 4 ML": 26.00,
        "TOMATOE 5 gram": 2.3,
        
    },

    "GOLDEN YAM": {
        "YAM 300 GRAMS": 500.00,
        "EGG 1 PCS": 150.00,
        "WHITE PEPPER 0.5 gram": 9.1,
        "SALT 0.5 gram": 0.38,
        "VEGETABLE OIL 250 ML": 0.00,
    },

    "SWEET POTATOES FRIED": {
        "SWEET POTATOES 300 GRAMS": 125.1,
        "SALT 0.5 gram": 0.38,
        "KETCHUP 10 ml": 44.8,
        "VEGETABLE OIL 250 ML": 530.00,
    },

    "BEANS CAKE (AKARA)": {
        "BEANS FLOUR 150 GRAM": 330.00,
        "SHUMBO 100 GRAM": 233.00,
        "ONIONS 50 GRAM": 68.00,
        "GARLIC 5 GRAM": 0.3,
        "GINGER 5 GRAM": 0.3,
        "CRAYFISH 15 GRAM": 75.00,
        "KNORR CUBE 2 GRAM": 21.00,
        "SALT 2 GRAM": 3.7,
        "PEPPER 2 GRAM": 7.00,
        "VEGETABLE OIL 250 ML": 0.00,
    },

    "RICE MASA": {
        "RICE GRAINS 127 GRAM": 166.00,
        "YEAST 4 GRAMS": 20.00,
        "BAKING POWDER 2 GRAMS": 7.00,
        "SALT 2 GRAM": 0.75,
        "KNORR CUBE 45 GRAM": 70.00,
        "VEGETABLE OIL 15 ML": 32.00,
       
    },

    "FRESH CORN & COCONUT": {
        "FRESH CORN 1 PCS": 400.00,
        "SALT 1 PINCH": 0.38,
        "COCONUT 1/2 RING": 350.00,
        
    },

    "MOI-MOI": {
        "BEANS FLOUR 150 GRAM": 330.00,
        "SHUMBO 2GRAM": 233.00,
        "ONIONS 50 GRAM": 68.00,
        "GARLIC 5 GRAM": 0.3,
        "GINGER 5 GRAM": 0.3,
        "VEGETABLE OIL 120ML": 254.00,
        "CRAYFISH 15 GRAM": 75.00,
        "KNORR CUBE 7.5 GRAM": 80.6,
        "SALT 2 GRAM": 3.7,
        "PEPPER 2 GRAM": 7.00,
        
    },

    "CUSTARD": {
        "CUSTARD POWDER 50 GRAM": 100.00,
        "SUGAR 15 GRAM": 30.00,
        "MILK 30 GRAM": 210.00,
        
    },

    "PAP (AKAMU)": {
        "MAIZE PASTE 30 GRAM": 120.00,
        "SUGAR 30": 30.00,
        "MILK 30 GRAM": 210.00,
        
    },

    "NIGERIAN PANCAKE": {
        "FLOUR 125 GRAM": 125.00,
        "BAKING POWDER 4 GRAM": 3.00,
        "NUTMEG 2 GRAM": 0.00,
        "SALT 0.5 GRAM": 0.38,
        "VEGETABLE OIL 15 ML": 32.00,
        "EGG 1 PCS": 150.00,
        "MILK 30 GRAM": 210.00,
        "SUGAR 15 GRAM": 30.00,
        "PEPPER 2 GRAM": 7.00,
        "ONIONS 50 GRAM": 68.00,
    },

    "FRIED PLANTAIN": {
        "Plantain 200 GRAM": 600.00,
        "salt 2 GRAM": 2.00,
        "Vegetable oil 15 ML": 32.00,
        
    },

    "SIRISH POTATOE & SWEET POTATOE CHIPS": {
        "Irish or sweet potato 300 G": 600.00,
        "Salt 2 GRAM": 2.00,
        "Vegetable oil 15 ML": 32.00,
        
    },

    "SIDE BEANS": {
        "BROWN BEANS 200 GRAM": 800.00,
        
    },

    "FRIED CHICKEN": {
        "CHICKEN (CUT 4) 400 GRAM": 1120.00,
        "VEGETABLE OIL 30 ML": 63.6,
        "ONIONS (SORTEY) 30 GRAM": 40.8,
        "KNORR CUBE 2.14 GRAM": 23.00,
    },

    "FRIED GOAT MEAT": {
        "GOAT MEAT (3 PCS) 250 GRAM": 912.5,
        "VEGETABLE OIL 30 ML": 63.6,
        "ONIONS (SORTEY) 30 GRAM": 40.8,
        "KNORR CUBE 2.14 GRAM": 23.00,
    },

    "FRIED BEEF": {
        "BEEF (3 PCS) CUT 12 250 GRAM": 850.00,
        "VEGETABLE OIL 30 ML": 63.6,
        "ONIONS (SORTEY) 30 GRAM": 40.8,
        "KNORR CUBE 2.14 GRAM": 23.00,
    },

    "FRIED CAT FISH": {
        "CAT FISH (CUT 3) 433.33 GRAM": 1300.00,
        "VEGETABLE OIL 30 ML": 63.6,
        "ONIONS (SORTEY) 30 GRAM": 40.8,
        "KNORR CUBE 2.14 GRAM": 23.00,
    },

    "FRIED COW TAIL": {
        "COW TAIL 250 GRAM": 1375.00,
        "VEGETABLE OIL 30 ML": 63.6,
        "ONIONS (SORTEY) 30 GRAM": 40.8,
        "KNORR CUBE 2.14 GRAM": 23.00,
    },

    "FRIED CROACKER FISH": {
        "FISH (CUT 3) 433.33 GRAM": 1300.00,
        "VEGETABLE OIL 30 ML": 63.6,
        "ONIONS (SORTEY) 30 GRAM": 40.8,
        "KNORR CUBE 2.14 GRAM": 23.00,
    },

    "FRIED TILLAPIA": {
        "FISH (CUT 3) 433.33 GRAM": 1840.00,
        "VEGETABLE OIL 30 ML": 63.6,
        "ONIONS (SORTEY) 30 GRAM": 40.8,
        "KNORR CUBE 2.14 GRAM": 23.00,
    },

    "FRIED GIZZARD": {
        "GIZZARD 300 GRAM": 900.00,
        "VEGETABLE OIL 30 ML": 63.6,
        "ONIONS (SORTEY) 30 GRAM": 40.8,
        "KNORR CUBE 2.14 GRAM": 23.00,
    },

    "ASSORTED": {
        "GIZZARD 300 GRAMS": 1350.00,
        "VEGETABLE OIL 30 ML": 63.6,
        "ONIONS (SORTEY) 30 GRAM": 40.8,
        "KNORR CUBE 2.14 GRAM": 23.00,
    },

    "CHICKEN LUNCHEON": {
        "CHICKEN LUNCHEON 200 gram": 1176.00,
        "OLIVE OIL 15 ML": 218.00,
        "SWEET CHILLI 2 ML": 9.00,
        "OYSTER SAUCE 2 ML": 8.00,
        "WHITE/BLACK PEPPER 1 gram": 42.00,
    },

    "CHICKEN SANDWICH": {
        "BREAD (FLOUR) 50 GRAM": 76.00,
        "CHICKEN BREAST 80 GRAM": 240.00,
        "LUNCHEON 50 GRAM": 441.00,
        "OLIVE OIL 15 ML": 218.00,
        "BENNY SPICE 0.5 gram": 5.70,
        "MAYONNAISE 95 GRAM": 352.00,
        "KETCHUP 10 GRAM": 65.00,
        "SUGAR 4 GRAM": 6.00,
        "FRESH TOMATOE 5 gram": 2.3,
        "SAUSAGE 1PCS": 100.00,
        "CABBAGE 10 GRAM": 50.00,
        "LETTUCE 10 GRAM": 30.00,
        "CARROT 10 GRAM": 7.00,
        "LETTUCE 10 GRAM": 30.00,
        "BOIL EGG 1 PCS": 150.00,
        "SLICED CHEESE 10 GRAM": 240.00,
        "FRIED IRISH POTATOE 100 GRAM": 91.6,
        "KETCHUP 4 ML": 26.00,
        "TOMATOE ": 2.3,
        "OLIVE SEED 6 PCS": 0.00,
    },

    "PEPPERED CHICKEN": {
        "CHICKEN (CUT 4) 400 GRAM": 1120.00,
        "VEGETABLE OIL 30 ML": 63.6,
        "ONIONS (SORTEY) 30 GRAM": 40.8,
        "FRESH TOMATOES 100 GRAM": 105.00,
        "TOMATOE PASTE 4.28 GRAM": 9.8,
        "DRY PEPPER 4.28 GRAM": 29.7,
        "KNORR CUBE 2.14 GRAM": 23.00,
        "ONIONS 20 GRAM": 27.00,
    },

    "PEPPERED GOAT MEAT": {
        "GOAT MEAT (3 PCS) 250 GRAM": 912.5,
        "VEGETABLE OIL 30 ML": 63.6,
        "ONIONS (SORTEY) 30 GRAM": 40.8,
        "FRESH TOMATOES v": 105.00,
        "TOMATOE PASTE 4.28 GRAM": 9.8,
        "DRY PEPPER 4.28 GRAM": 29.7,
        "KNORR CUBE 2.14 GRAM": 23.00,
        "ONIONS 20.GRAM": 27.00,
        
    },

    "PEPPERED BEEF": {
        "BEEF (3 PCS) CUT 12 250 GRAM": 850.00,
        "VEGETABLE OIL 30 ML": 63.6,
        "ONIONS (SORTEY) 30 GRAM": 40.8,
        "FRESH TOMATOES 100 GRAM": 105.00,
        "TOMATOE PASTE 4.28 GRAM": 9.8,
        "DRY PEPPER 4.28 GRAM": 29.7,
        "KNORR CUBE 2.14 GRAM": 23.00,
        "ONIONS 20.GRAM": 27.00,
        
    },

    "PEPPERED CAT FISH": {
        "CAT FISH (CUT 3) 433.33 GRAM": 1300.00,
        "VEGETABLE OIL 30 ML": 63.6,
        "ONIONS (SORTEY) 30 GRAM": 40.8,
        "FRESH TOMATOES 100 GRAM": 105.00,
        "TOMATOE PASTE 4.28 GRAM": 9.8,
        "DRY PEPPER 4.28 GRAM": 29.7,
        "KNORR CUBE 2.14 GRAM": 23.00,
        "ONIONS 20.GRAM": 27.00,
        
    },

    "COW TAIL": {
        "COW TAIL 250 GRAM": 1375.00,
        "VEGETABLE OIL 30 ML": 63.6,
        "ONIONS (SORTEY) 30 GRAM": 40.8,
        "FRESH TOMATOES 100 GRAM": 105.00,
        "TOMATOE PASTE 4.28 GRAM": 9.8,
        "DRY PEPPER 4.28 GRAM": 29.7,
        "KNORR CUBE 2.14 GRAM": 23.00,
        "ONIONS 20.GRAM": 27.00,
        
    },

    "CROACKER FISH": {
        "CAT FISH (CUT 3) 433.33 GRAM": 1300.00,
        "VEGETABLE OIL 30 ML": 63.6,
        "ONIONS (SORTEY) 30 GRAM": 40.8,
        "FRESH TOMATOES 100 GRAM": 105.00,
        "TOMATOE PASTE 4.28 GRAM": 9.8,
        "DRY PEPPER 4.28 GRAM": 29.7,
        "KNORR CUBE 2.14 GRAM": 23.00,
        "ONIONS 20.GRAM": 27.00,
    },

    "PEPPERED TILLAPIA": {
        "FISH (CUT 3) 433.33 GRAM": 1840.00,
        "VEGETABLE OIL 30 ML": 63.6,
        "ONIONS (SORTEY) 30 GRAM": 40.8,
        "FRESH TOMATOES 100 GRAM": 105.00,
        "TOMATOE PASTE 4.28 GRAM": 9.8,
        "DRY PEPPER 4.28 GRAM": 29.7,
        "KNORR CUBE 2.14 GRAM": 23.00,
        "ONIONS 20.GRAM": 27.00,
    },

    "PEPPERED SNAIL": {
        "SNAIL 300 GRAM": 900.00,
        "VEGETABLE OIL 30 ML": 63.6,
        "ONIONS (SORTEY) 30 GRAM": 40.8,
        "FRESH TOMATOES 100 GRAM": 105.00,
        "TOMATOE PASTE 4.28 GRAM": 9.8,
        "DRY PEPPER 4.28 GRAM": 29.7,
        "KNORR CUBE 2.14 GRAM": 23.00,
        "ONIONS 20.GRAM": 27.00,
        
    },

    "PEPPERED ASSORTED": {
        "INTESTINE 300 GRAMS": 1350.00,
        "VEGETABLE OIL 30 ML": 63.6,
        "ONIONS (SORTEY) 30 GRAM": 40.8,
        "FRESH TOMATOES 100 GRAM": 105.00,
        "TOMATOE PASTE 4.28 GRAM": 9.8,
        "DRY PEPPER 4.28 GRAM": 29.7,
        "KNORR CUBE 2.14 GRAM": 23.00,
        "ONIONS 20.GRAM": 27,
        
    },

    "PEPPERED CHICKEN WINGS": {
        "GIZZARD 400 GRAMS": 1280.00,
        "VEGETABLE OIL v": 63.6,
        "ONIONS (SORTEY) 30 GRAM": 40.8,
        "FRESH TOMATOES 100 GRAM": 105.00,
        "TOMATOE PASTE 4.28 GRAM": 9.8,
        "DRY PEPPER 4.28 GRAM": 29.7,
        "KNORR CUBE 2.14 GRAM": 23.00,
        "ONIONS 20.GRAM": 27.00,
        
    },

    "PEPPERED GIZZARD": {
        "GIZZARD 300 GRAMS": 960.00,
        "VEGETABLE OIL 30 ML": 63.6,
        "ONIONS (SORTEY) 30 GRAM": 40.8,
        "FRESH TOMATOES 100 GRAM": 105.00,
        "TOMATOE PASTE 4.28 GRAM": 9.8,
        "DRY PEPPER 4.28 GRAM": 29.7,
        "KNORR CUBE v": 23.00,
        "ONIONS 20.GRAM": 27.00,
        
    },

    "PEPPERED DRY FISH": {
        "DRY FISH 200 GRAM": 2000.00,
        "VEGETABLE OIL 30 ML": 63.6,
        "ONIONS (SORTEY) 30 GRAM": 40.8,
        "FRESH TOMATOES 100 GRAM": 105.00,
        "TOMATOE PASTE 4.28 GRAM": 9.80,
        "DRY PEPPER 4.28 GRAM": 29.7,
        "KNORR CUBE 2.14 GRAM": 23.00,
        "ONIONS 20.GRAM": 27.00,
        
    },

    "SHRIMPS": {
        "SHRIMPS 150 GRAMS": 1770.00,
        "OLIVE OIL v": 435.00,
        "GARLIC 10 GRAM": 54.00,
        "ONIONS 20 GRAM": 10.7,
        "SWEET CHILLI v": 44.00,
        "OYSTER SAUCE 2 ML": 7.8,
        "CORN STARCH 4 ML": 8.3,
        "WHITE/ BLACK PEPPER 0.5 GRAM": 20.8,
        "KNORR CUBE 0.5 gram": 5.3,
        
    },

    "PRAWNS": {
        "PRAWNS 150 GRAMS": 1770.00,
        "OLIVE OIL 30 ML": 435.00,
        "GARLIC v": 54.00,
        "ONIONS 20 GRAM": 20.7,
        "SWEET CHILLI 10 ML": 44.00,
        "OYSTER SAUCE 2 ML": 7.8,
        "CORN STARCH 4 ML": 8.3,
        "WHITE/ BLACK PEPPER 0.5 GRAM": 20.8,
        "KNORR CUBE 0.5 gram": 5.3,
        
    },

    "CALAMARI": {
        "CALAMARI 200 GRAMS": 2360.00,
        "OLIVE OIL 30 ML": 435.00,
        "GARLIC 10 GRAM": 54.00,
        "ONIONS 20 GRAM": 10.7,
        "SWEET CHILLI 10 ML": 44.00,
        "OYSTER SAUCE 2 ML": 7.8,
        "CORN STARCH 4 ML": 8.3,
        "WHITE/ BLACK PEPPER 0.5 GRAM": 20.8,
        "KNORR CUBE 0.5 gram": 5.3,
        
    },

    "GOAT MEAT PEPPER SOUP": {
        "GOAT MEAT (3 PCS) 250 GRAM": 912.5,
        "IRISH POTATOE 40 GRAM": 36.00,
        "CRISPAN SPECIAL SPICE 3 GRAM": 9.00,
        "GARLIC 3 GRAM": 0.16,
        "ONIONS 20 GRAM": 27.00,
        "GINGER 4 GRAM": 0.22,
        "AIDAN FRUIT PINCH": 3.00,
        "SCENT LEAF 6 GRAM": 3.00,
        "UZIZA LEAF 4 GRAM": 16.00,
        "PEPPER 4 GRAM": 13.8,
        "KNORR CUBE 2 GRAM": 21.00,
        "SHUMBO (BELL PEPPER) 1.6 GRAM": 5.53,
        "CURRY 2.5 GRAM": 14.00,
        "EHURU 0.5 GRAM": 6.00,
        
    },

    "COW TAIL PEPPER SOUP": {
        "COW TAIL 250 GRAM": 1375.00,
        "IRISH POTATOE 40 GRAM": 36.00,
        "CRISPAN SPECIAL SPICE 3 GRAM": 9.00,
        "GARLIC 3 GRAM": 0.16,
        "ONIONS 20 GRAM": 27.00,
        "GINGER 4 GRAM": 0.22,
        "AIDAN FRUIT PINCH": 3.00,
        "SCENT LEAF 6 GRAM": 3.00,
        "UZIZA LEAF 4 GRAM": 16.00,
        "PEPPER 4 GRAM": 13.8,
        "KNORR CUBE 2 GRAM": 21.00,
        "CURRY 2.5 GRAM": 14.00,
        "EHURU 0.5 GRAM": 6.00,
        
    },

    "CAT FISH PEPPER SOUP": {
        "CAT FISH (CUT 3) 433.33 GRAM": 1300.00,
        "IRISH POTATOE 40 GRAM": 36.00,
        "CRISPAN SPECIAL SPICE 3 GRAM": 9.00,
        "GARLIC 3 GRAM": 0.16,
        "ONIONS 20 GRAM": 27.00,
        "GINGER 4 GRAM": 0.22,
        "AIDAN FRUIT 0.5 GRAM": 3.00,
        "SCENT LEAF 6 GRAM": 3.00,
        "UZIZA LEAF 4 GRAM": 16.00,
        "PEPPER 4 GRAM": 13.8,
        "KNORR CUBE GRAM": 21.00,
        "CURRY 2.5 GRAM": 14.00,
        "EHURU 0.5 GRAM": 6.00,
        
    },

    "BEEF PEPPER SOUP": {
        "BEEF (3 PCS) CUT 12 250 GRAM": 850.00,
        "IRISH POTATOE 40 GRAM": 36.00,
        "CRISPAN SPECIAL SPICE 3 GRAM": 9.00,
        "GARLIC 3 GRAM": 0.16,
        "ONIONS 20 GRAM": 27.00,
        "GINGER 4 GRAM": 0.22,
        "AIDAN FRUIT 0.5 GRAM": 3.00,
        "SCENT LEAF 6 GRAM": 3.00,
        "UZIZA LEAF 4 GRAM": 16.00,
        "PEPPER 4 GRAM": 13.8,
        "KNORR CUBE 8 GRAM": 21.00,
        "SHUMBO (BELL PEPPER) 1.6 GRAM": 5.53,
        "CURRY 2.5 GRAM": 14.00,
        "EHURU 0.5 GRAM": 6.00,
        
    },

    "CHICKEN PEPPER SOUP": {
        "CHICKEN (CUT 4) 400 GRAM": 1120.00,
        "IRISH POTATOE 40 GRAM": 36.00,
        "CRISPAN SPECIAL SPICE 3 GRAM": 9.00,
        "GARLIC 3 GRAM": 0.16,
        "ONIONS 20 GRAM": 27.00,
        "GINGER 4 GRAM": 0.22,
        "AIDAN FRUIT PINCH": 3.00,
        "SCENT LEAF 6 GRAM": 3.00,
        "UZIZA LEAF 4 GRAM": 16.00,
        "PEPPER 4 GRAM": 13.8,
        "KNORR CUBE 2 GRAM": 21.00,
        "SHUMBO (BELL PEPPER) 1.6 GRAM": 5.53,
        "CURRY 2.5 GRAM": 14.00,
        "EHURU 0.5 GRAM": 6.00,
        
    },

    "COW LEG PEPPER SOUP": {
        "COW LEG PEPPER SOUP 250 GRAM": 1225.00,
        "IRISH POTATOE 40 GRAM": 36.00,
        "CRISPAN SPECIAL SPICE 3 GRAM": 9.00,
        "GARLIC 3 GRAM": 0.16,
        "ONIONS 20 GRAM": 27.00,
        "GINGER 4 GRAM": 0.22,
        "AIDAN FRUIT PINCH": 3.00,
        "SCENT LEAF 6 GRAM": 3.00,
        "UZIZA LEAF 4 GRAM": 16.00,
        "PEPPER 4 GRAM": 13.8,
        "KNORR CUBE 2 GRAM": 21.00,
        "SHUMBO (BELL PEPPER) 1.6 GRAM": 5.53,
        "CURRY 2.5 GRAM": 14.00,
        "EHURU 0.5 GRAM": 6.00,
        
    },

    "DRY FISH PEPPER SOUP": {
        "DRY FISH 300 GRAM": 3000.00,
        "IRISH POTATOE 40 GRAM": 36.00,
        "CRISPAN SPECIAL SPICE 3 GRAM": 9.00,
        "GARLIC 3 GRAM": 0.16,
        "ONIONS 20 GRAM": 27.00,
        "GINGER 4 GRAM": 0.22,
        "AIDAN FRUIT 0.5 GRAM": 3.00,
        "SCENT LEAF 6 GRAM": 3.00,
        "UZIZA LEAF 4 GRAM": 16.00,
        "PEPPER 4 GRAM": 13.8,
        "KNORR CUBE 2 GRAM": 21.00,
        "CURRY 2.5 GRAM": 14.00,
        "EHURU 0.5 GRAM": 6.00,
        
    },

    "ASSORTED PEPPER SOUP": {
        "INTESTINE 300 GRAMS": 1350.00,
        "IRISH POTATOE 40 GRAM": 36.00,
        "CRISPAN SPECIAL SPICE 3 GRAM": 9.00,
        "GARLIC 3 GRAM": 0.16,
        "ONIONS 20 GRAM": 27.00,
        "GINGER 4 GRAM": 0.22,
        "AIDAN FRUIT 0.5 GRAM": 3.00,
        "SCENT LEAF 6 GRAM": 3.00,
        "UZIZA LEAF 4 GRAM": 16.00,
        "PEPPER 4 GRAM": 13.8,
        "KNORR CUBE 2 GRAM": 21.00,
        "CURRY 2.5 GRAM": 14.00,
        "EHURU 0.5 GRAM": 6.00,
        
    },

    "CROACKER FISH PEPPER SOUP": {
        "CAT FISH (CUT 3) 433.33 GRAM": 1300.00,
        "IRISH POTATOE 40 GRAM": 36.00,
        "CRISPAN SPECIAL SPICE 3 GRAM": 9.00,
        "GARLIC 3 GRAM": 0.16,
        "ONIONS 20 GRAM": 27.00,
        "GINGER 4 GRAM": 0.22,
        "AIDAN FRUIT 0.5 GRAM": 3.00,
        "SCENT LEAF 6 GRAM": 3.00,
        "UZIZA LEAF 4 GRAM": 16.00,
        "PEPPER 4 GRAM": 13.8,
        "KNORR CUBE GRAM": 21.00,
        "CURRY 2.5 GRAM": 14.00,
        "EHURU 0.5 GRAM": 6.00,
        
    },

    "FRITATA": {
        "BACON 200 GRAMS": 1000.00,
        "EGG 1 PCS": 150.00,
        "MILK 4 GRAMS": 26.00,
        "BUTTER 15 GRAMS": 94.00,
        "SALT 2 GRAMS": 0.38,
        "BLACK PEPPER 0.5 GRAM": 20.8,
        "CHEESE 10 GRAMS": 550.00,
        
    },

    "INFUSED WATER": {
        "WATERMELON 1/10": 250.00,
        "ORANGE 1 PCS": 100.00,
        "LIME 1/2": 50.00,
        "BLACK BAILEYS 1CL": 278.6,
        "STRAWBERRY 2PCS": 200.00,
    },

    "WATERMELON JUICE": {
        "WATERMELON 2/10": 500.00,
        
    },

    "EWEDU SOUP": {
        "EWEDU LEAF 300 GRAM": 200.00,
        "DRY FISH 70 GRAM": 279.00,
        "CRAY FISH 4 GRAM": 2000,
        "YORUBA DAWA-DAWA 0.5 GRAM": 50.00,
        "KNORR CUBE 4 GRAM": 43.00,
        "SALT PINCH": 0.38,
        
    },

    "EFORIRO SOUP": {
        "SPINASH 300 GRAM": 300.00,
        "FRESH TOMATOE 50 GRAM": 18.00,
        "DRY FISH 40 GRAM": 371.40,
        "KPOMO 62.5 GRAM": 62.5,
        "CRAYFISH 4 GRAM": 20.00,
        "PALM OIL 75 ML": 102.00,
        "INTESTINE 300 GRAM": 1350.00,
        "DAWA-DAWA 0.5 GRAM": 50.00,
        "PEPPER 4 GRAM": 13.00,
        "ONIONS 20 GRAM": 27.00,
        "SALT PINCH": 0.38,
        "KNORR CUBE 4 GRAM": 43.00,
    },

    "KUKA SOUP": {
        "DRY KUKA": 125.00,
        "SHAMBO 4 GRAM": 13.00,
        "PEPPER 4 GRAM": 13.00,
        "DRY FISH 40 GRAM": 371.4,
        "ONIONS 30 GRAM": 40.00,
        "PALM OIL 90 ML": 122.4,
        "DAWA-DAWA 0.5 GRAM": 50.00,
        "CRAYFISH 4 GRAM": 20.00,
        "SALT PINCH": 0.38,
        "KNORR CUBE 4 GRAM": 43.00,
    },

    "WAFFLES": {
        "FLOUR 66.7 GRAM": 85.4,
        "BUTTER 13.3 GRAM": 59.00,
        "SUGAR 13.3 GRAM": 22.4,
        "MILK 6.7 GRAM": 46.1,
        "EGG 0.07 PCS": 10.00,
        "BAKING POWDER 0.25 TTSP": 3.3,
    },

    "SLICED CAKE": {
        "FLOUR 14.3 GRAM": 18.3,
        "BUTTER 10 GRAM": 44.24,
        "MILK 1.43 GRAM": 9.88,
        "SUGAR 3.6 GRAM": 6.00,
        "EGG 0.2 PCS": 32.00,
        "MILK FLAVOUR 1.4 GRAM": 18.00,
        "BAKING POWDER 0.014 TTSP": 0.8,
        "PRESERVATIVES 0.011 TTSP": 1.00,
        "NUTMEG 0.05 TTSP": 0.29,
    },

    "FRUITE CAKE": {
        "FLOUR 166.7 GRAM": 213.5,
        "SUGAR 83.3 GRAM": 140.00,
        "BUTTER 116.7 GRAM": 516.13,
        "EGG 2.5 PCS": 375.00,
        "BAKING POWDER 0.25 TTSP": 8.3,
        "PRESERVATIVES 0.011 TTSP": 1.00,
        "MILK 16.7 GRAM": 115.3,
        "MILK FLAVOUR 1.4 GRAM": 18.00,
        "DRY FRUITE 33.3 GRAM": 417.00,
    }

}

# CSS for icons and styling
st.markdown("""
    <style>
        /* General page styles */
        .main { background-color: #f8f9fa; }

        /* Header styles */
        h1, h2, h3 { color: #2C3E50; font-family: 'Arial', sans-serif; }

        /* General text color */
        body, p, span, div { color: #2C3E50; }

        /* Navigation icons */
        .menu-icon { margin-right: 10px; }

        /* Block container styling */
        .block-container {
            padding: 2rem 1rem;
            max-width: 80%;
            margin: auto;
            background: #ffffff;
            color: #2C3E50;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }

        /* Sidebar styling */
        .css-1d391kg { background-color: #1E3A8A; color: white; }
        .css-1d391kg h2 { color: white; }

        /* Button styling */
        button { border-radius: 5px; background-color: #4CAF50; color: white; font-weight: bold; padding: 10px; border: none; }
        button:hover { background-color: #45a049; }
    </style>
""", unsafe_allow_html=True)



# App Header
st.image("LOGO.png", use_container_width=True)
st.title("Menu Engineering Calculator")
st.markdown("Welcome to the **Menu Engineering Calculator**! This app helps you manage and calculate the costs of menu items in a professional and efficient way. 🎉")

# Sidebar Navigation
st.sidebar.title("Navigation")
menu_options = [
    "📊 Calculate Menu Cost",
    "🛠️ Manage Menu Cost",
    "📜 View Menu Cost List"
]
selected_option = st.sidebar.radio("Choose an action:", menu_options)

# Functionality: Calculate BOM
if selected_option == "📊 Calculate Menu Cost":
    st.header("📊 Calculate Bill of Material")

    # Search bar for menu items
    search_query = st.text_input("Search for a Menu Item").strip().lower()

    # Filter menu items based on search query
    filtered_menu_items = [item for item in menu_data.keys() if search_query in item.lower()]

    # Menu item dropdown with filtered results
    if filtered_menu_items:
        selected_menu = st.selectbox("Select a Menu Item", [""] + filtered_menu_items)
    else:
        st.warning("No menu items match your search.")
        selected_menu = None

    # Calculate and display BOM details
    if selected_menu:
        components = menu_data.get(selected_menu, {})
        total_cost = sum(components.values())

        st.write(f"### Menu Cost for {selected_menu}")
        st.write("#### Components and Costs")

        for item, cost in components.items():
            st.write(f"- {item}: ₦{cost:.2f}")

        st.success(f"### Total Cost: ₦{total_cost:.2f}")

# Functionality: Manage BOM
if selected_option == "🛠️ Manage Menu Cost":
    st.header("🛠️ Manage Menu Costing")
    st.markdown("Use the fields below to add or update a menu item and its components.")

    # Input fields for managing BOM
    menu_item = st.text_input("Menu Item")
    component_name = st.text_input("Component Name")
    component_cost = st.text_input("Cost (₦)")

    if st.button("Add/Update Cost"):
        if menu_item and component_name and component_cost:
            try:
                component_cost = float(component_cost)
                if menu_item not in menu_data:
                    menu_data[menu_item] = {}
                menu_data[menu_item][component_name] = component_cost
                st.success(f"Component '{component_name}' added/updated for '{menu_item}'.")
            except ValueError:
                st.error("Cost must be a numeric value.")
        else:
            st.error("All fields are required.")

# Functionality: View BOM List
if selected_option == "📜 View Menu Cost List":
    st.header("📜 View Menu Cost of Materials")
    st.markdown("Below is a list of all menu items and their components.")

    for menu, components in menu_data.items():
        st.subheader(menu)
        for item, cost in components.items():
            st.write(f"- {item}: ₦{cost:.2f}")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #888888; font-size: 12px;">
        Designed with ❤️ for Professional Standards<br>
        &copy; 2025 - CRISPAN Suite & Event Center Jos.
    </div>
    """, unsafe_allow_html=True
)
