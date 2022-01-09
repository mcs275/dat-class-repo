{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img src=\"http://imgur.com/1ZcRyrc.png\" style=\"float: left; margin: 20px; height: 55px\">\n",
    "\n",
    "# Project 2: Analyzing IMDb Data\n",
    "\n",
    "_Author: Kevin Markham (DC)_\n",
    "\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "For project two, you will complete a series of exercises exploring movie rating data from IMDb.\n",
    "\n",
    "For these exercises, you will be conducting basic exploratory data analysis on IMDB's movie data, looking to answer such questions as:\n",
    "\n",
    "What is the average rating per genre?\n",
    "How many different actors are in a movie?\n",
    "\n",
    "This process will help you practice your data analysis skills while becoming comfortable with Pandas."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Basic level"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Read in 'imdb_1000.csv' and store it in a DataFrame named movies."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>star_rating</th>\n",
       "      <th>title</th>\n",
       "      <th>content_rating</th>\n",
       "      <th>genre</th>\n",
       "      <th>duration</th>\n",
       "      <th>actors_list</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>9.3</td>\n",
       "      <td>The Shawshank Redemption</td>\n",
       "      <td>R</td>\n",
       "      <td>Crime</td>\n",
       "      <td>142</td>\n",
       "      <td>[u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>9.2</td>\n",
       "      <td>The Godfather</td>\n",
       "      <td>R</td>\n",
       "      <td>Crime</td>\n",
       "      <td>175</td>\n",
       "      <td>[u'Marlon Brando', u'Al Pacino', u'James Caan']</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>9.1</td>\n",
       "      <td>The Godfather: Part II</td>\n",
       "      <td>R</td>\n",
       "      <td>Crime</td>\n",
       "      <td>200</td>\n",
       "      <td>[u'Al Pacino', u'Robert De Niro', u'Robert Duv...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>9.0</td>\n",
       "      <td>The Dark Knight</td>\n",
       "      <td>PG-13</td>\n",
       "      <td>Action</td>\n",
       "      <td>152</td>\n",
       "      <td>[u'Christian Bale', u'Heath Ledger', u'Aaron E...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>8.9</td>\n",
       "      <td>Pulp Fiction</td>\n",
       "      <td>R</td>\n",
       "      <td>Crime</td>\n",
       "      <td>154</td>\n",
       "      <td>[u'John Travolta', u'Uma Thurman', u'Samuel L....</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   star_rating                     title content_rating   genre  duration  \\\n",
       "0          9.3  The Shawshank Redemption              R   Crime       142   \n",
       "1          9.2             The Godfather              R   Crime       175   \n",
       "2          9.1    The Godfather: Part II              R   Crime       200   \n",
       "3          9.0           The Dark Knight          PG-13  Action       152   \n",
       "4          8.9              Pulp Fiction              R   Crime       154   \n",
       "\n",
       "                                         actors_list  \n",
       "0  [u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...  \n",
       "1    [u'Marlon Brando', u'Al Pacino', u'James Caan']  \n",
       "2  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...  \n",
       "3  [u'Christian Bale', u'Heath Ledger', u'Aaron E...  \n",
       "4  [u'John Travolta', u'Uma Thurman', u'Samuel L....  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies = pd.read_csv('./data/imdb_1000.csv')\n",
    "movies.head()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Check the number of rows and columns."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(979, 6)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Check the data type of each column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 979 entries, 0 to 978\n",
      "Data columns (total 6 columns):\n",
      " #   Column          Non-Null Count  Dtype  \n",
      "---  ------          --------------  -----  \n",
      " 0   star_rating     979 non-null    float64\n",
      " 1   title           979 non-null    object \n",
      " 2   content_rating  976 non-null    object \n",
      " 3   genre           979 non-null    object \n",
      " 4   duration        979 non-null    int64  \n",
      " 5   actors_list     979 non-null    object \n",
      "dtypes: float64(1), int64(1), object(4)\n",
      "memory usage: 46.0+ KB\n"
     ]
    }
   ],
   "source": [
    "movies.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Calculate the average movie duration."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "120.97957099080695"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies['duration'].mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Sort the DataFrame by duration to find the shortest and longest movies."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "star_rating                                                     7.8\n",
      "title                                                        Hamlet\n",
      "content_rating                                                PG-13\n",
      "genre                                                         Drama\n",
      "duration                                                        242\n",
      "actors_list       [u'Kenneth Branagh', u'Julie Christie', u'Dere...\n",
      "Name: 476, dtype: object star_rating                                                     8.0\n",
      "title                                                        Freaks\n",
      "content_rating                                              UNRATED\n",
      "genre                                                         Drama\n",
      "duration                                                         64\n",
      "actors_list       [u'Wallace Ford', u'Leila Hyams', u'Olga Bacla...\n",
      "Name: 389, dtype: object\n"
     ]
    }
   ],
   "source": [
    "idmax=movies['duration'].idxmax()\n",
    "idmin=movies['duration'].idxmin()\n",
    "print(movies.iloc[idmax],  \n",
    "      movies.iloc[idmin])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Create a histogram of duration, choosing an \"appropriate\" number of bins."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([  7.,  18.,  54., 114., 149., 152., 143., 116.,  76.,  35.,  37.,\n",
       "         29.,  16.,  11.,  10.,   4.,   2.,   3.,   1.,   2.]),\n",
       " array([ 64. ,  72.9,  81.8,  90.7,  99.6, 108.5, 117.4, 126.3, 135.2,\n",
       "        144.1, 153. , 161.9, 170.8, 179.7, 188.6, 197.5, 206.4, 215.3,\n",
       "        224.2, 233.1, 242. ]),\n",
       " <BarContainer object of 20 artists>)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "d=movies.duration\n",
    "plt.hist(d,bins=20)\n",
    "\n",
    "#how to decided on the \"appropriate\" Number of bins???. start with 10 and observe the pattern to avoid missing out patterns. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Use a box plot to display that same data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'whiskers': [<matplotlib.lines.Line2D at 0x7fa05ebf50a0>,\n",
       "  <matplotlib.lines.Line2D at 0x7fa05ebf5400>],\n",
       " 'caps': [<matplotlib.lines.Line2D at 0x7fa05ebf5760>,\n",
       "  <matplotlib.lines.Line2D at 0x7fa05ebf5ac0>],\n",
       " 'boxes': [<matplotlib.lines.Line2D at 0x7fa05ecbed00>],\n",
       " 'medians': [<matplotlib.lines.Line2D at 0x7fa05ebf5e20>],\n",
       " 'fliers': [<matplotlib.lines.Line2D at 0x7fa05ec031c0>],\n",
       " 'means': []}"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.boxplot(d)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Intermediate level"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Count how many movies have each of the content ratings."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "content_rating\n",
       "APPROVED      47\n",
       "G             32\n",
       "GP             3\n",
       "NC-17          7\n",
       "NOT RATED     65\n",
       "PASSED         7\n",
       "PG           123\n",
       "PG-13        189\n",
       "R            460\n",
       "TV-MA          1\n",
       "UNRATED       38\n",
       "X              4\n",
       "Name: title, dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c=movies.groupby('content_rating')['title'].count()\n",
    "c\n",
    "##more information here: https://www.analyticsvidhya.com/blog/2020/03/groupby-pandas-aggregating-data-python/"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Use a visualization to display that same data, including a title and x and y labels."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:title={'center':'# of movies per Content rating'}, xlabel='content_rating', ylabel='movie count'>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "c.plot.bar(title='# of movies per Content rating', ylabel='movie count')\n",
    "\n",
    "#plotting in series function."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Convert the following content ratings to \"UNRATED\": NOT RATED, APPROVED, PASSED, GP."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "star_rating       160\n",
       "title             160\n",
       "content_rating    160\n",
       "genre             160\n",
       "duration          160\n",
       "actors_list       160\n",
       "dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies['content_rating']=movies['content_rating'].replace(['NOT RATED','APPROVED','PASSED','GP'],'UNRATED')\n",
    "movies[movies['content_rating']=='UNRATED'].count()\n",
    "##replace"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Convert the following content ratings to \"NC-17\": X, TV-MA."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "star_rating       12\n",
       "title             12\n",
       "content_rating    12\n",
       "genre             12\n",
       "duration          12\n",
       "actors_list       12\n",
       "dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies['content_rating']=movies['content_rating'].replace(['X','TV-MA'],'NC-17')\n",
    "movies[movies['content_rating']=='NC-17'].count()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Count the number of missing values in each column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "star_rating       0\n",
       "title             0\n",
       "content_rating    3\n",
       "genre             0\n",
       "duration          0\n",
       "actors_list       0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### If there are missing values: examine them, then fill them in with \"reasonable\" values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "star_rating       0\n",
       "title             0\n",
       "content_rating    0\n",
       "genre             0\n",
       "duration          0\n",
       "actors_list       0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies.loc[movies['content_rating'].isnull(),'content_rating']=\"UNRATED\"\n",
    "movies.isnull().sum()\n",
    "#Reference Extra_pandas_cleaning "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Calculate the average star rating for movies 2 hours or longer, and compare that with the average star rating for movies shorter than 2 hours."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.11023201174742514"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a=movies[movies['duration']>=120]['star_rating'].mean()\n",
    "b=movies[movies['duration']<120]['star_rating'].mean()\n",
    "a-b"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
<<<<<<< HEAD
    "**Jonathan's Note:** You can do a groupby with this in one line:  `movies.groupby(movies['duration'] > 120)['star_rating'].mean()` and get a cleaner result."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
=======
>>>>>>> 47b2484ce0a32c8c37275f0354207e26eb222815
    "#### Use a visualization to detect whether there is a relationship between duration and star rating."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x7fa05eedb3d0>"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(movies['duration'],movies['star_rating'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Calculate the average duration for each genre."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "genre\n",
       "Action       126.485294\n",
       "Adventure    134.840000\n",
       "Animation     96.596774\n",
       "Biography    131.844156\n",
       "Comedy       107.602564\n",
       "Crime        122.298387\n",
       "Drama        126.539568\n",
       "Family       107.500000\n",
       "Fantasy      112.000000\n",
       "Film-Noir     97.333333\n",
       "History       66.000000\n",
       "Horror       102.517241\n",
       "Mystery      115.625000\n",
       "Sci-Fi       109.000000\n",
       "Thriller     114.200000\n",
       "Western      136.666667\n",
       "Name: duration, dtype: float64"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies.groupby('genre')['duration'].mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Advanced level"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Visualize the relationship between content rating and duration."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "hovertemplate": "content_rating=%{x}<br>duration=%{y}<extra></extra>",
         "legendgroup": "",
         "marker": {
          "color": "#636efa",
          "pattern": {
           "shape": ""
          }
         },
         "name": "",
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": false,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "G",
          "NC-17",
          "PG",
          "PG-13",
          "R",
          "UNRATED"
         ],
         "xaxis": "x",
         "y": [
          112.34375,
          116.25,
          115.30081300813008,
          127.19576719576719,
          122.16304347826087,
          116.76073619631902
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "barmode": "relative",
        "height": 300,
        "legend": {
         "tracegroupgap": 0
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "content rating vs. duration"
        },
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "content_rating"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "duration"
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"59ee4178-7a3c-475a-9775-01cbe42024a1\" class=\"plotly-graph-div\" style=\"height:300px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"59ee4178-7a3c-475a-9775-01cbe42024a1\")) {                    Plotly.newPlot(                        \"59ee4178-7a3c-475a-9775-01cbe42024a1\",                        [{\"alignmentgroup\":\"True\",\"hovertemplate\":\"content_rating=%{x}<br>duration=%{y}<extra></extra>\",\"legendgroup\":\"\",\"marker\":{\"color\":\"#636efa\",\"pattern\":{\"shape\":\"\"}},\"name\":\"\",\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"textposition\":\"auto\",\"x\":[\"G\",\"NC-17\",\"PG\",\"PG-13\",\"R\",\"UNRATED\"],\"xaxis\":\"x\",\"y\":[112.34375,116.25,115.30081300813008,127.19576719576719,122.16304347826087,116.76073619631902],\"yaxis\":\"y\",\"type\":\"bar\"}],                        {\"template\":{\"data\":{\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"content_rating\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"duration\"}},\"legend\":{\"tracegroupgap\":0},\"title\":{\"text\":\"content rating vs. duration\"},\"barmode\":\"relative\",\"height\":300},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('59ee4178-7a3c-475a-9775-01cbe42024a1');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import plotly.express as px\n",
    "df = movies.groupby('content_rating').mean().reset_index()\n",
    "px.bar(df, x='content_rating', y='duration', title='content rating vs. duration', height = 300)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Determine the top rated movie (by star rating) for each genre."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>star_rating</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>genre</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Action</th>\n",
       "      <td>Yojimbo</td>\n",
       "      <td>9.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Adventure</th>\n",
       "      <td>True Grit</td>\n",
       "      <td>8.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Animation</th>\n",
       "      <td>Wreck-It Ralph</td>\n",
       "      <td>8.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Biography</th>\n",
       "      <td>Walk the Line</td>\n",
       "      <td>8.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Comedy</th>\n",
       "      <td>Zombieland</td>\n",
       "      <td>8.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Crime</th>\n",
       "      <td>Zodiac</td>\n",
       "      <td>9.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Drama</th>\n",
       "      <td>Zulu</td>\n",
       "      <td>8.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Family</th>\n",
       "      <td>Willy Wonka &amp; the Chocolate Factory</td>\n",
       "      <td>7.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Fantasy</th>\n",
       "      <td>The City of Lost Children</td>\n",
       "      <td>7.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Film-Noir</th>\n",
       "      <td>The Third Man</td>\n",
       "      <td>8.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>History</th>\n",
       "      <td>Battleship Potemkin</td>\n",
       "      <td>8.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Horror</th>\n",
       "      <td>[Rec]</td>\n",
       "      <td>8.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mystery</th>\n",
       "      <td>Vertigo</td>\n",
       "      <td>8.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Sci-Fi</th>\n",
       "      <td>The Day the Earth Stood Still</td>\n",
       "      <td>8.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Thriller</th>\n",
       "      <td>The Man Who Knew Too Much</td>\n",
       "      <td>8.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Western</th>\n",
       "      <td>Unforgiven</td>\n",
       "      <td>8.9</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                         title  star_rating\n",
       "genre                                                      \n",
       "Action                                 Yojimbo          9.0\n",
       "Adventure                            True Grit          8.9\n",
       "Animation                       Wreck-It Ralph          8.6\n",
       "Biography                        Walk the Line          8.9\n",
       "Comedy                              Zombieland          8.6\n",
       "Crime                                   Zodiac          9.3\n",
       "Drama                                     Zulu          8.9\n",
       "Family     Willy Wonka & the Chocolate Factory          7.9\n",
       "Fantasy              The City of Lost Children          7.7\n",
       "Film-Noir                        The Third Man          8.3\n",
       "History                    Battleship Potemkin          8.0\n",
       "Horror                                   [Rec]          8.6\n",
       "Mystery                                Vertigo          8.6\n",
       "Sci-Fi           The Day the Earth Stood Still          8.2\n",
       "Thriller             The Man Who Knew Too Much          8.0\n",
       "Western                             Unforgiven          8.9"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies.groupby('genre')[['title','star_rating']].max()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Check if there are multiple movies with the same title, and if so, determine if they are actually duplicates."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>star_rating</th>\n",
       "      <th>title</th>\n",
       "      <th>content_rating</th>\n",
       "      <th>genre</th>\n",
       "      <th>duration</th>\n",
       "      <th>actors_list</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>482</th>\n",
       "      <td>7.8</td>\n",
       "      <td>The Girl with the Dragon Tattoo</td>\n",
       "      <td>R</td>\n",
       "      <td>Crime</td>\n",
       "      <td>152</td>\n",
       "      <td>[u'Michael Nyqvist', u'Noomi Rapace', u'Ewa Fr...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>905</th>\n",
       "      <td>7.5</td>\n",
       "      <td>Dracula</td>\n",
       "      <td>R</td>\n",
       "      <td>Horror</td>\n",
       "      <td>128</td>\n",
       "      <td>[u'Gary Oldman', u'Winona Ryder', u'Anthony Ho...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>924</th>\n",
       "      <td>7.5</td>\n",
       "      <td>Les Miserables</td>\n",
       "      <td>PG-13</td>\n",
       "      <td>Crime</td>\n",
       "      <td>134</td>\n",
       "      <td>[u'Liam Neeson', u'Geoffrey Rush', u'Uma Thurm...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>936</th>\n",
       "      <td>7.4</td>\n",
       "      <td>True Grit</td>\n",
       "      <td>UNRATED</td>\n",
       "      <td>Adventure</td>\n",
       "      <td>128</td>\n",
       "      <td>[u'John Wayne', u'Kim Darby', u'Glen Campbell']</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     star_rating                            title content_rating      genre  \\\n",
       "482          7.8  The Girl with the Dragon Tattoo              R      Crime   \n",
       "905          7.5                          Dracula              R     Horror   \n",
       "924          7.5                   Les Miserables          PG-13      Crime   \n",
       "936          7.4                        True Grit        UNRATED  Adventure   \n",
       "\n",
       "     duration                                        actors_list  \n",
       "482       152  [u'Michael Nyqvist', u'Noomi Rapace', u'Ewa Fr...  \n",
       "905       128  [u'Gary Oldman', u'Winona Ryder', u'Anthony Ho...  \n",
       "924       134  [u'Liam Neeson', u'Geoffrey Rush', u'Uma Thurm...  \n",
       "936       128    [u'John Wayne', u'Kim Darby', u'Glen Campbell']  "
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies[movies['title'].duplicated()]\n",
    "\n",
    "#duplicated note will only show one of the 2 duplicates!"
   ]
  },
  {
<<<<<<< HEAD
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Jonathan's Note:** There is an argument for this method called `keep`, and if you set this to `False` it will show all of the values that are showing up as duplicated, and you can see that they are not.  They have the same title but are made in different years."
   ]
  },
  {
=======
>>>>>>> 47b2484ce0a32c8c37275f0354207e26eb222815
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>star_rating</th>\n",
       "      <th>title</th>\n",
       "      <th>content_rating</th>\n",
       "      <th>genre</th>\n",
       "      <th>duration</th>\n",
       "      <th>actors_list</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>662</th>\n",
       "      <td>7.7</td>\n",
       "      <td>True Grit</td>\n",
       "      <td>PG-13</td>\n",
       "      <td>Adventure</td>\n",
       "      <td>110</td>\n",
       "      <td>[u'Jeff Bridges', u'Matt Damon', u'Hailee Stei...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>936</th>\n",
       "      <td>7.4</td>\n",
       "      <td>True Grit</td>\n",
       "      <td>UNRATED</td>\n",
       "      <td>Adventure</td>\n",
       "      <td>128</td>\n",
       "      <td>[u'John Wayne', u'Kim Darby', u'Glen Campbell']</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     star_rating      title content_rating      genre  duration  \\\n",
       "662          7.7  True Grit          PG-13  Adventure       110   \n",
       "936          7.4  True Grit        UNRATED  Adventure       128   \n",
       "\n",
       "                                           actors_list  \n",
       "662  [u'Jeff Bridges', u'Matt Damon', u'Hailee Stei...  \n",
       "936    [u'John Wayne', u'Kim Darby', u'Glen Campbell']  "
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies[movies['title']=='The Girl with the Dragon Tattoo']\n",
    "movies[movies['title']=='Dracula']\n",
    "movies[movies['title']=='Les Miserables']\n",
    "movies[movies['title']=='True Grit']\n",
    "\n",
    "# all have different durations and actor list, likely different versions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>star_rating</th>\n",
       "      <th>title</th>\n",
       "      <th>content_rating</th>\n",
       "      <th>genre</th>\n",
       "      <th>duration</th>\n",
       "      <th>actors_list</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: [star_rating, title, content_rating, genre, duration, actors_list]\n",
       "Index: []"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#or check for all duplicated, which returns none. If there is duplicate, drop_duplicates()\n",
    "movies[movies.duplicated()]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "#### Calculate the average star rating for each genre, but only include genres with at least 10 movies\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Option 1: manually create a list of relevant genres, then filter using that list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "genre\n",
       "Action       7.884559\n",
       "Adventure    7.933333\n",
       "Animation    7.914516\n",
       "Biography    7.862338\n",
       "Comedy       7.822436\n",
       "Crime        7.916935\n",
       "Drama        7.902518\n",
       "Horror       7.806897\n",
       "Mystery      7.975000\n",
       "Name: star_rating, dtype: float64"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies['genre'].value_counts()>=10\n",
    "movies[movies['genre'].isin (['Drama','Comedy','Action','Crime','Biography','Adventure','Animation','Horror','Mystery'])].groupby('genre')['star_rating'].mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
<<<<<<< HEAD
    "**Jonathan's Note:** To avoid typing this out statically, you could get the index for the query `movies['genre'].value_counts() >= 10` and then pass that into the `isin` method.  \n",
    "\n",
    "So something like:\n",
    "\n",
    "`genres = movies['genre'].value_counts(); more_than_ten = genres[genres > 10].index; ` and then pass the result of that into `isin`.  A little more programmatic."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
=======
>>>>>>> 47b2484ce0a32c8c37275f0354207e26eb222815
    "#### Option 2: automatically create a list of relevant genres by saving the value_counts and then filtering"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "genre\n",
       "Action       7.884559\n",
       "Adventure    7.933333\n",
       "Animation    7.914516\n",
       "Biography    7.862338\n",
       "Comedy       7.822436\n",
       "Crime        7.916935\n",
       "Drama        7.902518\n",
       "Horror       7.806897\n",
       "Mystery      7.975000\n",
       "Name: star_rating, dtype: float64"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1 = movies['genre'].value_counts()>10\n",
    "df1 = df1.to_frame()\n",
    "df1 = df1[df1.genre].reset_index()\n",
    "goodlist = df1.iloc[:,0].to_list()\n",
    "movies[movies['genre'].isin(goodlist)].groupby('genre')['star_rating'].mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Option 3: calculate the average star rating for all genres, then filter using a boolean Series"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>star_rating</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>genre</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Action</th>\n",
       "      <td>7.884559</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Adventure</th>\n",
       "      <td>7.933333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Animation</th>\n",
       "      <td>7.914516</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Biography</th>\n",
       "      <td>7.862338</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Comedy</th>\n",
       "      <td>7.822436</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Crime</th>\n",
       "      <td>7.916935</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Drama</th>\n",
       "      <td>7.902518</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Horror</th>\n",
       "      <td>7.806897</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mystery</th>\n",
       "      <td>7.975000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           star_rating\n",
       "genre                 \n",
       "Action        7.884559\n",
       "Adventure     7.933333\n",
       "Animation     7.914516\n",
       "Biography     7.862338\n",
       "Comedy        7.822436\n",
       "Crime         7.916935\n",
       "Drama         7.902518\n",
       "Horror        7.806897\n",
       "Mystery       7.975000"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "full=movies[['genre','star_rating']].groupby('genre').mean()\n",
    "count=movies[['genre','star_rating']].groupby('genre').count()\n",
    "full[count>=10].dropna()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Option 4: aggregate by count and mean, then filter using the count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>star_rating</th>\n",
       "      <th>count</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>genre</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Action</th>\n",
       "      <td>7.884559</td>\n",
       "      <td>136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Adventure</th>\n",
       "      <td>7.933333</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Animation</th>\n",
       "      <td>7.914516</td>\n",
       "      <td>62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Biography</th>\n",
       "      <td>7.862338</td>\n",
       "      <td>77</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Comedy</th>\n",
       "      <td>7.822436</td>\n",
       "      <td>156</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Crime</th>\n",
       "      <td>7.916935</td>\n",
       "      <td>124</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Drama</th>\n",
       "      <td>7.902518</td>\n",
       "      <td>278</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Horror</th>\n",
       "      <td>7.806897</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mystery</th>\n",
       "      <td>7.975000</td>\n",
       "      <td>16</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           star_rating  count\n",
       "genre                        \n",
       "Action        7.884559    136\n",
       "Adventure     7.933333     75\n",
       "Animation     7.914516     62\n",
       "Biography     7.862338     77\n",
       "Comedy        7.822436    156\n",
       "Crime         7.916935    124\n",
       "Drama         7.902518    278\n",
       "Horror        7.806897     29\n",
       "Mystery       7.975000     16"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "w = movies[['genre','star_rating']].groupby('genre').mean()\n",
    "w['count']=movies[['genre','star_rating']].groupby('genre').count()\n",
    "w[w['count']>=10]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Bonus"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "#### Figure out something \"interesting\" using the actors data!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-114-8a44e449e4b6>:3: FutureWarning:\n",
      "\n",
      "The default value of regex will change from True to False in a future version. In addition, single character regular expressions will*not* be treated as literal strings when regex=True.\n",
      "\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "0      3\n",
       "1      3\n",
       "2      3\n",
       "3      3\n",
       "4      3\n",
       "      ..\n",
       "464    3\n",
       "465    3\n",
       "466    3\n",
       "467    3\n",
       "468    3\n",
       "Name: actors_list, Length: 469, dtype: int64"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "avg=movies['star_rating'].mean()\n",
    "goodmovies = movies[movies['star_rating']>avg]\n",
    "goodmovies['actors_list'].str.replace('[','').replace(']','').str.split(',').str.len()\n",
    "\n",
    "#all movies have 3 actors listed in the table among movies with a rating above average"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>star_rating</th>\n",
       "      <th>title</th>\n",
       "      <th>content_rating</th>\n",
       "      <th>genre</th>\n",
       "      <th>duration</th>\n",
       "      <th>actors_list</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>9.3</td>\n",
       "      <td>The Shawshank Redemption</td>\n",
       "      <td>R</td>\n",
       "      <td>Crime</td>\n",
       "      <td>142</td>\n",
       "      <td>[u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>8.7</td>\n",
       "      <td>Se7en</td>\n",
       "      <td>R</td>\n",
       "      <td>Drama</td>\n",
       "      <td>127</td>\n",
       "      <td>[u'Morgan Freeman', u'Brad Pitt', u'Kevin Spac...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>119</th>\n",
       "      <td>8.3</td>\n",
       "      <td>Unforgiven</td>\n",
       "      <td>R</td>\n",
       "      <td>Western</td>\n",
       "      <td>131</td>\n",
       "      <td>[u'Clint Eastwood', u'Gene Hackman', u'Morgan ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>227</th>\n",
       "      <td>8.1</td>\n",
       "      <td>Million Dollar Baby</td>\n",
       "      <td>PG-13</td>\n",
       "      <td>Drama</td>\n",
       "      <td>132</td>\n",
       "      <td>[u'Hilary Swank', u'Clint Eastwood', u'Morgan ...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     star_rating                     title content_rating    genre  duration  \\\n",
       "0            9.3  The Shawshank Redemption              R    Crime       142   \n",
       "24           8.7                     Se7en              R    Drama       127   \n",
       "119          8.3                Unforgiven              R  Western       131   \n",
       "227          8.1       Million Dollar Baby          PG-13    Drama       132   \n",
       "\n",
       "                                           actors_list  \n",
       "0    [u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...  \n",
       "24   [u'Morgan Freeman', u'Brad Pitt', u'Kevin Spac...  \n",
       "119  [u'Clint Eastwood', u'Gene Hackman', u'Morgan ...  \n",
       "227  [u'Hilary Swank', u'Clint Eastwood', u'Morgan ...  "
      ]
     },
     "execution_count": 122,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#and how many times Morgan Freeman appeared? \n",
    "\n",
    "query = goodmovies['actors_list'].str.lower().str.contains('morgan freeman')\n",
    "goodmovies.loc[query]\n",
    "\n",
    "# He showed up in 4 movies!"
   ]
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
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
<<<<<<< HEAD
   "version": "3.8.5"
=======
   "version": "3.8.8"
>>>>>>> 47b2484ce0a32c8c37275f0354207e26eb222815
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
