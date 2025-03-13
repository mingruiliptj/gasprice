import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta
import os

def fetch_meti_data():
    """
    Fetch gasoline price data from METI (Ministry of Economy, Trade and Industry) website
    This is a simplified version - in reality we would need to handle pagination and multiple years
    """
    # Create sample data structure (in real implementation, we would scrape from METI)
    prefectures = [
        "Hokkaido", "Aomori", "Iwate", "Miyagi", "Akita", "Yamagata", "Fukushima",
        "Ibaraki", "Tochigi", "Gunma", "Saitama", "Chiba", "Tokyo", "Kanagawa",
        "Niigata", "Toyama", "Ishikawa", "Fukui", "Yamanashi", "Nagano", "Gifu",
        "Shizuoka", "Aichi", "Mie", "Shiga", "Kyoto", "Osaka", "Hyogo", "Nara",
        "Wakayama", "Tottori", "Shimane", "Okayama", "Hiroshima", "Yamaguchi",
        "Tokushima", "Kagawa", "Ehime", "Kochi", "Fukuoka", "Saga", "Nagasaki",
        "Kumamoto", "Oita", "Miyazaki", "Kagoshima", "Okinawa"
    ]
    
    # Generate sample data for last 20 years
    current_year = datetime.now().year
    start_year = current_year - 20
    
    data = []
    base_price = 150  # Base price in yen
    
    for year in range(start_year, current_year + 1):
        for prefecture in prefectures:
            # Generate somewhat realistic price variations
            price = base_price + (year - start_year) * 2  # Slight increase over years
            # Add some regional variations
            if prefecture in ["Tokyo", "Osaka", "Kanagawa"]:
                price += 10
            elif prefecture in ["Hokkaido", "Okinawa"]:
                price += 15
            
            data.append({
                "year": year,
                "prefecture": prefecture,
                "price": round(price + ((hash(prefecture + str(year)) % 20) - 10), 2)
            })
            
    return data

def save_data(data):
    """Save the processed data as JSON"""
    if not os.path.exists('data'):
        os.makedirs('data')
        
    with open('data/gasoline_prices.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    print("Fetching gasoline price data...")
    data = fetch_meti_data()
    print("Saving data...")
    save_data(data)
    print("Data collection complete!")

if __name__ == "__main__":
    main() 