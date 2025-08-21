import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# --- 1. Synthetic Data Generation ---
np.random.seed(42) # for reproducibility
# Sample data representing brand posts and customer comments
data = {
    'Post': ['New Product Launch!', 'Sustainability Initiative', 'Behind the Scenes', 'Customer Review 1', 'Customer Review 2', 'New Campaign', 'Community Event'],
    'BrandSentiment': ['Positive', 'Positive', 'Positive', 'Positive', 'Positive', 'Positive', 'Positive'],
    'CustomerSentiment': ['Positive', 'Neutral', 'Positive', 'Negative', 'Positive', 'Negative', 'Positive'],
    'Engagement': np.random.randint(100, 1000, size=7)
}
df = pd.DataFrame(data)
# --- 2. Analysis ---
# Calculate the frequency of different sentiment combinations
sentiment_counts = df.groupby(['BrandSentiment', 'CustomerSentiment'])['Post'].count().unstack()
# Identify discrepancies (where BrandSentiment and CustomerSentiment differ)
discrepancies = sentiment_counts.copy()
np.fill_diagonal(discrepancies.values, 0) #Zero out the diagonal to only show discrepancies
# --- 3. Visualization ---
plt.figure(figsize=(10, 6))
sns.heatmap(discrepancies, annot=True, cmap="coolwarm", fmt="d", linewidths=.5)
plt.title('Brand vs. Customer Sentiment Discrepancies')
plt.xlabel('Customer Sentiment')
plt.ylabel('Brand Sentiment')
plt.tight_layout()
#Save the plot to a file
output_filename = 'sentiment_discrepancies.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")
#Further analysis (example):  Calculate the percentage of discrepancies
total_posts = len(df)
percentage_discrepancies = (discrepancies.sum().sum() / total_posts) * 100
print(f"\nPercentage of Sentiment Discrepancies: {percentage_discrepancies:.2f}%")
#Example of adding more data for a more robust analysis.  This is optional and doesn't change the core functionality.
more_data = {
    'Post': ['New Product Launch!','Behind the Scenes', 'Customer Review 3', 'Customer Review 4'],
    'BrandSentiment': ['Positive', 'Positive', 'Positive', 'Positive'],
    'CustomerSentiment': ['Positive', 'Neutral', 'Negative', 'Negative'],
    'Engagement': np.random.randint(100,1000, size=4)
}
df2 = pd.DataFrame(more_data)
df = pd.concat([df, df2], ignore_index=True)
#Repeat analysis and visualization with the added data (optional)
sentiment_counts = df.groupby(['BrandSentiment', 'CustomerSentiment'])['Post'].count().unstack()
discrepancies = sentiment_counts.copy()
np.fill_diagonal(discrepancies.values, 0)
plt.figure(figsize=(10, 6))
sns.heatmap(discrepancies, annot=True, cmap="coolwarm", fmt="d", linewidths=.5)
plt.title('Brand vs. Customer Sentiment Discrepancies (Updated)')
plt.xlabel('Customer Sentiment')
plt.ylabel('Brand Sentiment')
plt.tight_layout()
output_filename2 = 'sentiment_discrepancies_updated.png'
plt.savefig(output_filename2)
print(f"Plot saved to {output_filename2}")
total_posts = len(df)
percentage_discrepancies = (discrepancies.sum().sum() / total_posts) * 100
print(f"\nPercentage of Sentiment Discrepancies (Updated): {percentage_discrepancies:.2f}%")