import pandas as pd
# import data
facebook = pd.read_parquet('facebook_post_insights.parquet')
instagram = pd.read_parquet("instagram_post_insights (1).parquet")
df1 = facebook.set_index('created_time')
df2 = instagram.set_index('created_time')
df1.add(df2)
result = df1.merge(df2, on=['created_time'], how='outer')

df_out = result.reset_index()
cols = ['created_time', 'message_x', 'shares', 'reactions', 'likes',
       'comments', 'post_impressions', 'post_impressions_unique',
       'post_engaged_users', 'post_engaged_fan', 'post_impressions_fan_unique',
       'post_impressions_organic_unique', 'post_reactions_like_total',
       'account_x', 'message_y',
       'saved', 'engagement', 'impressions', 'reach', 'views', 'account_y',
       'created_y', 'like_count']

cols_used = ['message', 'account', 'created_time', 'shares', 'reactions', 'likes', 'comments',
       'saved', 'engagement', 'impressions', 'reach', 'views', 'account', 'like_count']
df_out = df_out.fillna('')
df_out['message'] = df_out['message_x'] + df_out['message_y']
df_out['account'] = df_out['account_x'] + df_out['account_y']
df_out[cols_used].to_csv('posts_incl_scores.csv')