{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "outputs": [],
   "source": [
    "# import data\n",
    "facebook = pd.read_parquet('facebook_post_insights.parquet')\n",
    "instagram = pd.read_parquet(\"instagram_post_insights (1).parquet\")"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                  id        created_time  \\\n",
      "0    360787567740895_169125415395341 2021-09-25 08:45:37   \n",
      "1    106407221316278_163181198972213 2021-03-16 09:59:47   \n",
      "2    146644665960101_148455524130874 2021-09-03 14:53:27   \n",
      "3    360787567740895_608870356938016 2021-09-25 17:45:22   \n",
      "4  1739550549695812_2940531222931066 2021-09-16 16:57:31   \n",
      "\n",
      "                                             message shares  reactions  likes  \\\n",
      "0  Over hele Europa stiller Volt op til lokalvalg...   None          8      7   \n",
      "1  Laat de status quo achter je. Stem vernieuwend...      4         20     17   \n",
      "2  Op 26 September zijn er verkiezingen in Duitsl...      9        164    159   \n",
      "3                                               None   None          2      2   \n",
      "4  Over the last two years, our movement has grow...      8         97     88   \n",
      "\n",
      "   comments  post_impressions  post_impressions_unique  post_engaged_users  \\\n",
      "0         1             123.0                    121.0                 9.0   \n",
      "1         5            1330.0                   1164.0                52.0   \n",
      "2         7            6436.0                   6389.0               344.0   \n",
      "3         0               0.0                      0.0                 0.0   \n",
      "4         5            5142.0                   5142.0               155.0   \n",
      "\n",
      "   post_engaged_fan  post_impressions_fan_unique  \\\n",
      "0               8.0                         84.0   \n",
      "1              26.0                        185.0   \n",
      "2             189.0                       4837.0   \n",
      "3               0.0                          0.0   \n",
      "4             117.0                       4196.0   \n",
      "\n",
      "   post_impressions_organic_unique  post_reactions_like_total  \\\n",
      "0                            121.0                        7.0   \n",
      "1                           1164.0                       22.0   \n",
      "2                           6389.0                      175.0   \n",
      "3                              0.0                        0.0   \n",
      "4                           5142.0                      100.0   \n",
      "\n",
      "            account        created permalink_url  \n",
      "0      Volt Danmark  20211027_0000          None  \n",
      "1  Nilüfer Gündoğan  20211029_0000          None  \n",
      "2    Volt Nederland  20211029_0000          None  \n",
      "3      Volt Danmark  20211029_0000          None  \n",
      "4       Volt Europa  20211029_0000          None  \n",
      "Index(['id', 'created_time', 'message', 'shares', 'reactions', 'likes',\n",
      "       'comments', 'post_impressions', 'post_impressions_unique',\n",
      "       'post_engaged_users', 'post_engaged_fan', 'post_impressions_fan_unique',\n",
      "       'post_impressions_organic_unique', 'post_reactions_like_total',\n",
      "       'account', 'created', 'permalink_url'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(facebook.head())\n",
    "print(facebook.columns)"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0       Over hele Europa stiller Volt op til lokalvalg...\n",
      "1       Laat de status quo achter je. Stem vernieuwend...\n",
      "2       Op 26 September zijn er verkiezingen in Duitsl...\n",
      "3                                                    None\n",
      "4       Over the last two years, our movement has grow...\n",
      "                              ...                        \n",
      "2710    Am heutigen Abstimmungssonntag hat die Schweiz...\n",
      "2711    Wofür steht Volt? Klar: Europa. 🇪🇺 \\n\\nAber wa...\n",
      "2712    Der er kun 13 måneder til Europaparlamentsvalg...\n",
      "2713    \"Wir sind damit so einen riesigen Schritt hin ...\n",
      "2714    Et liv i værdighed inkluderer en værdig død.\\n...\n",
      "Name: message, Length: 2715, dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(facebook.message)"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0       Do you feel comfortable and safe to express yo...\n",
      "1                                    A day at the office.\n",
      "2       O Volt Portugal exige a demissão imediata do p...\n",
      "3       Hoje celebra-se o dia o Dia Internacional da P...\n",
      "4       A campanha #countrymonth do #volteuropa  este ...\n",
      "                              ...                        \n",
      "2461    Política não pode ser só no papel! Está nas no...\n",
      "2462    Idag skal jeg foretræde for Folketingets Inden...\n",
      "2463    🌿🌆 Liquid 3: Die \"flüssige\" Lösung gegen Luftv...\n",
      "2464    Am heutigen Abstimmungssonntag hat die Schweiz...\n",
      "2465    Volt gibt Stimmfreigabe zur OECD Mindeststeuer...\n",
      "Name: message, Length: 2466, dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(instagram.message)"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "outputs": [],
   "source": [
    "lst_posts = []\n",
    "for item in list(instagram.message):\n",
    "    lst_posts.append(item)\n",
    "for item in list(facebook.message):\n",
    "    lst_posts.append(item)"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "outputs": [
    {
     "data": {
      "text/plain": "5181"
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(lst_posts)"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "outputs": [
    {
     "ename": "OSError",
     "evalue": "Cannot save file into a non-existent directory: 'D:\u000Bolt\\policy_chatbot-main\\deployment'",
     "output_type": "error",
     "traceback": [
      "\u001B[1;31m---------------------------------------------------------------------------\u001B[0m",
      "\u001B[1;31mOSError\u001B[0m                                   Traceback (most recent call last)",
      "Cell \u001B[1;32mIn[36], line 6\u001B[0m\n\u001B[0;32m      3\u001B[0m df \u001B[38;5;241m=\u001B[39m pd\u001B[38;5;241m.\u001B[39mDataFrame(\u001B[38;5;28mdict\u001B[39m)\n\u001B[0;32m      5\u001B[0m \u001B[38;5;66;03m# saving the dataframe\u001B[39;00m\n\u001B[1;32m----> 6\u001B[0m \u001B[43mdf\u001B[49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43mto_csv\u001B[49m\u001B[43m(\u001B[49m\u001B[38;5;124;43m'\u001B[39;49m\u001B[38;5;124;43mD:\u001B[39;49m\u001B[38;5;130;43;01m\\v\u001B[39;49;00m\u001B[38;5;124;43molt\u001B[39;49m\u001B[38;5;124;43m\\\u001B[39;49m\u001B[38;5;124;43mpolicy_chatbot-main\u001B[39;49m\u001B[38;5;124;43m\\\u001B[39;49m\u001B[38;5;124;43mdeployment\u001B[39;49m\u001B[38;5;124;43m\\\u001B[39;49m\u001B[38;5;124;43mposts.csv\u001B[39;49m\u001B[38;5;124;43m'\u001B[39;49m\u001B[43m)\u001B[49m\n",
      "File \u001B[1;32mD:\\volt\\policy_chatbot-main\\.venv\\lib\\site-packages\\pandas\\core\\generic.py:3902\u001B[0m, in \u001B[0;36mNDFrame.to_csv\u001B[1;34m(self, path_or_buf, sep, na_rep, float_format, columns, header, index, index_label, mode, encoding, compression, quoting, quotechar, lineterminator, chunksize, date_format, doublequote, escapechar, decimal, errors, storage_options)\u001B[0m\n\u001B[0;32m   3891\u001B[0m df \u001B[38;5;241m=\u001B[39m \u001B[38;5;28mself\u001B[39m \u001B[38;5;28;01mif\u001B[39;00m \u001B[38;5;28misinstance\u001B[39m(\u001B[38;5;28mself\u001B[39m, ABCDataFrame) \u001B[38;5;28;01melse\u001B[39;00m \u001B[38;5;28mself\u001B[39m\u001B[38;5;241m.\u001B[39mto_frame()\n\u001B[0;32m   3893\u001B[0m formatter \u001B[38;5;241m=\u001B[39m DataFrameFormatter(\n\u001B[0;32m   3894\u001B[0m     frame\u001B[38;5;241m=\u001B[39mdf,\n\u001B[0;32m   3895\u001B[0m     header\u001B[38;5;241m=\u001B[39mheader,\n\u001B[1;32m   (...)\u001B[0m\n\u001B[0;32m   3899\u001B[0m     decimal\u001B[38;5;241m=\u001B[39mdecimal,\n\u001B[0;32m   3900\u001B[0m )\n\u001B[1;32m-> 3902\u001B[0m \u001B[38;5;28;01mreturn\u001B[39;00m \u001B[43mDataFrameRenderer\u001B[49m\u001B[43m(\u001B[49m\u001B[43mformatter\u001B[49m\u001B[43m)\u001B[49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43mto_csv\u001B[49m\u001B[43m(\u001B[49m\n\u001B[0;32m   3903\u001B[0m \u001B[43m    \u001B[49m\u001B[43mpath_or_buf\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m   3904\u001B[0m \u001B[43m    \u001B[49m\u001B[43mlineterminator\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[43mlineterminator\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m   3905\u001B[0m \u001B[43m    \u001B[49m\u001B[43msep\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[43msep\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m   3906\u001B[0m \u001B[43m    \u001B[49m\u001B[43mencoding\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[43mencoding\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m   3907\u001B[0m \u001B[43m    \u001B[49m\u001B[43merrors\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[43merrors\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m   3908\u001B[0m \u001B[43m    \u001B[49m\u001B[43mcompression\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[43mcompression\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m   3909\u001B[0m \u001B[43m    \u001B[49m\u001B[43mquoting\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[43mquoting\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m   3910\u001B[0m \u001B[43m    \u001B[49m\u001B[43mcolumns\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[43mcolumns\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m   3911\u001B[0m \u001B[43m    \u001B[49m\u001B[43mindex_label\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[43mindex_label\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m   3912\u001B[0m \u001B[43m    \u001B[49m\u001B[43mmode\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[43mmode\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m   3913\u001B[0m \u001B[43m    \u001B[49m\u001B[43mchunksize\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[43mchunksize\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m   3914\u001B[0m \u001B[43m    \u001B[49m\u001B[43mquotechar\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[43mquotechar\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m   3915\u001B[0m \u001B[43m    \u001B[49m\u001B[43mdate_format\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[43mdate_format\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m   3916\u001B[0m \u001B[43m    \u001B[49m\u001B[43mdoublequote\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[43mdoublequote\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m   3917\u001B[0m \u001B[43m    \u001B[49m\u001B[43mescapechar\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[43mescapechar\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m   3918\u001B[0m \u001B[43m    \u001B[49m\u001B[43mstorage_options\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[43mstorage_options\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m   3919\u001B[0m \u001B[43m\u001B[49m\u001B[43m)\u001B[49m\n",
      "File \u001B[1;32mD:\\volt\\policy_chatbot-main\\.venv\\lib\\site-packages\\pandas\\io\\formats\\format.py:1152\u001B[0m, in \u001B[0;36mDataFrameRenderer.to_csv\u001B[1;34m(self, path_or_buf, encoding, sep, columns, index_label, mode, compression, quoting, quotechar, lineterminator, chunksize, date_format, doublequote, escapechar, errors, storage_options)\u001B[0m\n\u001B[0;32m   1131\u001B[0m     created_buffer \u001B[38;5;241m=\u001B[39m \u001B[38;5;28;01mFalse\u001B[39;00m\n\u001B[0;32m   1133\u001B[0m csv_formatter \u001B[38;5;241m=\u001B[39m CSVFormatter(\n\u001B[0;32m   1134\u001B[0m     path_or_buf\u001B[38;5;241m=\u001B[39mpath_or_buf,\n\u001B[0;32m   1135\u001B[0m     lineterminator\u001B[38;5;241m=\u001B[39mlineterminator,\n\u001B[1;32m   (...)\u001B[0m\n\u001B[0;32m   1150\u001B[0m     formatter\u001B[38;5;241m=\u001B[39m\u001B[38;5;28mself\u001B[39m\u001B[38;5;241m.\u001B[39mfmt,\n\u001B[0;32m   1151\u001B[0m )\n\u001B[1;32m-> 1152\u001B[0m \u001B[43mcsv_formatter\u001B[49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43msave\u001B[49m\u001B[43m(\u001B[49m\u001B[43m)\u001B[49m\n\u001B[0;32m   1154\u001B[0m \u001B[38;5;28;01mif\u001B[39;00m created_buffer:\n\u001B[0;32m   1155\u001B[0m     \u001B[38;5;28;01massert\u001B[39;00m \u001B[38;5;28misinstance\u001B[39m(path_or_buf, StringIO)\n",
      "File \u001B[1;32mD:\\volt\\policy_chatbot-main\\.venv\\lib\\site-packages\\pandas\\io\\formats\\csvs.py:247\u001B[0m, in \u001B[0;36mCSVFormatter.save\u001B[1;34m(self)\u001B[0m\n\u001B[0;32m    243\u001B[0m \u001B[38;5;250m\u001B[39m\u001B[38;5;124;03m\"\"\"\u001B[39;00m\n\u001B[0;32m    244\u001B[0m \u001B[38;5;124;03mCreate the writer & save.\u001B[39;00m\n\u001B[0;32m    245\u001B[0m \u001B[38;5;124;03m\"\"\"\u001B[39;00m\n\u001B[0;32m    246\u001B[0m \u001B[38;5;66;03m# apply compression and byte/text conversion\u001B[39;00m\n\u001B[1;32m--> 247\u001B[0m \u001B[38;5;28;01mwith\u001B[39;00m \u001B[43mget_handle\u001B[49m\u001B[43m(\u001B[49m\n\u001B[0;32m    248\u001B[0m \u001B[43m    \u001B[49m\u001B[38;5;28;43mself\u001B[39;49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43mfilepath_or_buffer\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m    249\u001B[0m \u001B[43m    \u001B[49m\u001B[38;5;28;43mself\u001B[39;49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43mmode\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m    250\u001B[0m \u001B[43m    \u001B[49m\u001B[43mencoding\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[38;5;28;43mself\u001B[39;49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43mencoding\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m    251\u001B[0m \u001B[43m    \u001B[49m\u001B[43merrors\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[38;5;28;43mself\u001B[39;49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43merrors\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m    252\u001B[0m \u001B[43m    \u001B[49m\u001B[43mcompression\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[38;5;28;43mself\u001B[39;49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43mcompression\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m    253\u001B[0m \u001B[43m    \u001B[49m\u001B[43mstorage_options\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[38;5;28;43mself\u001B[39;49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43mstorage_options\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m    254\u001B[0m \u001B[43m\u001B[49m\u001B[43m)\u001B[49m \u001B[38;5;28;01mas\u001B[39;00m handles:\n\u001B[0;32m    255\u001B[0m     \u001B[38;5;66;03m# Note: self.encoding is irrelevant here\u001B[39;00m\n\u001B[0;32m    256\u001B[0m     \u001B[38;5;28mself\u001B[39m\u001B[38;5;241m.\u001B[39mwriter \u001B[38;5;241m=\u001B[39m csvlib\u001B[38;5;241m.\u001B[39mwriter(\n\u001B[0;32m    257\u001B[0m         handles\u001B[38;5;241m.\u001B[39mhandle,\n\u001B[0;32m    258\u001B[0m         lineterminator\u001B[38;5;241m=\u001B[39m\u001B[38;5;28mself\u001B[39m\u001B[38;5;241m.\u001B[39mlineterminator,\n\u001B[1;32m   (...)\u001B[0m\n\u001B[0;32m    263\u001B[0m         quotechar\u001B[38;5;241m=\u001B[39m\u001B[38;5;28mself\u001B[39m\u001B[38;5;241m.\u001B[39mquotechar,\n\u001B[0;32m    264\u001B[0m     )\n\u001B[0;32m    266\u001B[0m     \u001B[38;5;28mself\u001B[39m\u001B[38;5;241m.\u001B[39m_save()\n",
      "File \u001B[1;32mD:\\volt\\policy_chatbot-main\\.venv\\lib\\site-packages\\pandas\\io\\common.py:739\u001B[0m, in \u001B[0;36mget_handle\u001B[1;34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001B[0m\n\u001B[0;32m    737\u001B[0m \u001B[38;5;66;03m# Only for write methods\u001B[39;00m\n\u001B[0;32m    738\u001B[0m \u001B[38;5;28;01mif\u001B[39;00m \u001B[38;5;124m\"\u001B[39m\u001B[38;5;124mr\u001B[39m\u001B[38;5;124m\"\u001B[39m \u001B[38;5;129;01mnot\u001B[39;00m \u001B[38;5;129;01min\u001B[39;00m mode \u001B[38;5;129;01mand\u001B[39;00m is_path:\n\u001B[1;32m--> 739\u001B[0m     \u001B[43mcheck_parent_directory\u001B[49m\u001B[43m(\u001B[49m\u001B[38;5;28;43mstr\u001B[39;49m\u001B[43m(\u001B[49m\u001B[43mhandle\u001B[49m\u001B[43m)\u001B[49m\u001B[43m)\u001B[49m\n\u001B[0;32m    741\u001B[0m \u001B[38;5;28;01mif\u001B[39;00m compression:\n\u001B[0;32m    742\u001B[0m     \u001B[38;5;28;01mif\u001B[39;00m compression \u001B[38;5;241m!=\u001B[39m \u001B[38;5;124m\"\u001B[39m\u001B[38;5;124mzstd\u001B[39m\u001B[38;5;124m\"\u001B[39m:\n\u001B[0;32m    743\u001B[0m         \u001B[38;5;66;03m# compression libraries do not like an explicit text-mode\u001B[39;00m\n",
      "File \u001B[1;32mD:\\volt\\policy_chatbot-main\\.venv\\lib\\site-packages\\pandas\\io\\common.py:604\u001B[0m, in \u001B[0;36mcheck_parent_directory\u001B[1;34m(path)\u001B[0m\n\u001B[0;32m    602\u001B[0m parent \u001B[38;5;241m=\u001B[39m Path(path)\u001B[38;5;241m.\u001B[39mparent\n\u001B[0;32m    603\u001B[0m \u001B[38;5;28;01mif\u001B[39;00m \u001B[38;5;129;01mnot\u001B[39;00m parent\u001B[38;5;241m.\u001B[39mis_dir():\n\u001B[1;32m--> 604\u001B[0m     \u001B[38;5;28;01mraise\u001B[39;00m \u001B[38;5;167;01mOSError\u001B[39;00m(\u001B[38;5;124mrf\u001B[39m\u001B[38;5;124m\"\u001B[39m\u001B[38;5;124mCannot save file into a non-existent directory: \u001B[39m\u001B[38;5;124m'\u001B[39m\u001B[38;5;132;01m{\u001B[39;00mparent\u001B[38;5;132;01m}\u001B[39;00m\u001B[38;5;124m'\u001B[39m\u001B[38;5;124m\"\u001B[39m)\n",
      "\u001B[1;31mOSError\u001B[0m: Cannot save file into a non-existent directory: 'D:\u000Bolt\\policy_chatbot-main\\deployment'"
     ]
    }
   ],
   "source": [
    "# dictionary of lists\n",
    "dict = {'message': lst_posts}\n",
    "df = pd.DataFrame(dict)\n",
    "\n",
    "# saving the dataframe\n",
    "df.to_csv('D:\\volt\\policy_chatbot-main\\deployment\\posts.csv')"
   ],
   "metadata": {
    "collapsed": false
   }
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "outputs": [],
   "source": [],
   "metadata": {
    "collapsed": false
   }
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
