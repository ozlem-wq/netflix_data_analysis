# utils.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def parse_date_added(df):
    """
    Veri çerçevesindeki 'date_added' sütununu datetime tipine dönüştürür
    ve yıl, ay bilgilerini çıkarır.
    """
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    df['month_added'] = df['date_added'].dt.month
    return df

def explode_listed_in(df, column='listed_in'):
    """
    Belirtilen sütundaki virgülle ayrılmış değerleri satırlara ayırır (explode).
    """
    df_temp = df.copy()
    df_temp[column] = df_temp[column].fillna('').astype(str).str.split(', ')
    return df_temp.explode(column)

def create_yearly_trend_chart(df, output_path=None):
    """
    Yıllara göre eklenen yapım sayısını gösteren bir çizgi grafik oluşturur.
    Grafiği ekranda gösterir ve belirtilen yola kaydeder.
    """
    yearly_counts = df['year_added'].value_counts().sort_index()

    plt.figure(figsize=(12, 6))
    sns.lineplot(x=yearly_counts.index, y=yearly_counts.values, marker='o')
    plt.title('Yıllara Göre Netflix\'e Eklenen Yapım Sayısı', fontsize=16)
    plt.xlabel('Yıl', fontsize=12)
    plt.ylabel('Yapım Sayısı', fontsize=12)
    plt.grid(True)
    plt.tight_layout()

    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        plt.savefig(output_path)
    
    plt.show()

def create_monthly_trend_chart(df, output_path=None):
    """
    Aylara göre eklenen yapım sayısını gösteren bir çizgi grafik oluşturur.
    Grafiği ekranda gösterir ve belirtilen yola kaydeder.
    """
    monthly_counts = df['month_added'].value_counts().sort_index()

    plt.figure(figsize=(12, 6))
    sns.lineplot(x=monthly_counts.index, y=monthly_counts.values, marker='o')
    plt.title('Aylara Göre Netflix\'e Eklenen Yapım Sayısı', fontsize=16)
    plt.xlabel('Ay', fontsize=12)
    plt.ylabel('Yapım Sayısı', fontsize=12)
    plt.grid(True)
    plt.tight_layout()

    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        plt.savefig(output_path)
    
    plt.show()

def create_top_genres_chart(df, output_path=None):
    """
    En çok geçen 15 türü gösteren bir bar grafik oluşturur.
    Grafiği ekranda gösterir ve belirtilen yola kaydeder.
    """
    expanded_df = explode_listed_in(df, column='listed_in')
    genre_counts = expanded_df['listed_in'].value_counts().head(15)

    plt.figure(figsize=(12, 8))
    sns.barplot(x=genre_counts.values, y=genre_counts.index, palette='viridis', hue=genre_counts.index, legend=False)
    plt.title('Netflix\'te En Çok Geçen 15 Tür', fontsize=16)
    plt.xlabel('Yapım Sayısı', fontsize=12)
    plt.ylabel('Tür', fontsize=12)
    plt.tight_layout()

    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        plt.savefig(output_path)
        
    plt.show()





