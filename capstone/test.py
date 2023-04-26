import pandas as pd
import streamlit as st
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity




# Add the Steam icon image


st.set_page_config(page_title = "GiantClip", page_icon = "🎮")
# Create a file uploader widget
uploaded_file = st.file_uploader("Choose your database", accept_multiple_files=False)

# Check if a file was uploaded
if uploaded_file is not None:
    # Read the contents of the file as a bytes object
    file_contents = uploaded_file.read()
    
    # Convert the bytes object to a pandas DataFrame
    games = pd.read_parquet(file_contents)
else:
    # If no file was uploaded, use a default database file
    games = pd.read_parquet("Bigclip.pq")
st.session_state.page = 0
def get_recommendations(game_profile, selected_genres=None, games=None):
    

    if selected_genres is not None:
        genres_lower = [genre.lower() for genre in selected_genres]
        game_profile += ', '.join(genres_lower)

    if games is None:
        games = pd.read_parquet('Bigclip1.pq')
        
    # Convert the game profile to a sparse matrix using TfidfVectorizer
    tfidf = TfidfVectorizer()
    sparse_matrix = tfidf.fit_transform(games['tags_description'])
    game_profile_vec = tfidf.transform([game_profile])
    
    # Compute the cosine similarity between the game profile and the game features
    game_similarities = cosine_similarity(sparse_matrix, game_profile_vec)
    
    # Sort the games by similarity score
    games['similarity_score'] = game_similarities
    sorted_games = games.sort_values(['similarity_score', 'positive_ratio', 'user_reviews'], ascending=False)

    game_games = [title.lower() for title in game_profile.split(', ')]
    sorted_games = sorted_games[~sorted_games['title'].str.lower().isin(game_games)]

    # Add Steam store URLs for each game
    sorted_games['Link'] = sorted_games['app_id'].apply(lambda x: f'<a href="https://store.steampowered.com/app/{x}" target="_blank">Link</a>')

    # Remove games with similarity score of 0
    sorted_games = sorted_games[sorted_games['similarity_score'] > 0]
    
    # Filter the recommendations by genre and rating
    if selected_genres:
        mask = sorted_games['tags'].apply(lambda x: any(tag in selected_genres for tag in x))
        sorted_games = sorted_games[mask]
    
    # Return the top 10 recommendations
    if len(sorted_games) > 0:
        return sorted_games.head(10)
    else:
        return None


def app():
    st.markdown('<img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Steam_2016_logo_black.svg" width="500">', unsafe_allow_html=True)
    st.title('Welcome to BigClip game recommendations!')
    st.write('Please input your games history, or select your preferred genres from the dropdown box.')

    # Add a text area for the user to input the game profile
    game_profile = st.text_area('Enter game tags or descriptions (separated by commas):')

    # Add a multiselect for the user to select preferred genres
    available_genres = sorted(set(tag for tags in games['tags'] for tag in tags))
    selected_genres = st.multiselect('Select your preferred genres:', available_genres)
    mac = st.checkbox('Mac user')
    linux = st.checkbox('Linux user')
    
    # Create a new variable to store the filtered games
    filtered_games = games.copy()

    # Filter the games based on the selected checkboxes
    if mac and linux:
        filtered_games = filtered_games[(filtered_games['Mac'] == 'Yes') & (filtered_games['Linux'] == 'Yes')]
    elif mac:
        filtered_games = filtered_games[filtered_games['Mac'] == 'Yes']
    elif linux:
        filtered_games = filtered_games[filtered_games['Linux'] == 'Yes']

    # Add a button to trigger the recommendation function
    if st.button('Get Recommendations'):
        st.session_state.page = 1
        recommendations = get_recommendations(game_profile, selected_genres, filtered_games)
        if recommendations is not None:
            recommendations_table = recommendations[['title', 'tags', 'Rating', 'description', 'Link']]
            recommendations_table = recommendations_table.rename(columns={"title": "Title", "tags": "Genre", "description": "Description"}).to_html(escape=False, index=False, table_id='recommendations', classes=['dataframe', 'my-table'], col_space='200px') 
            st.write(f'You might like these games')
            st.write(recommendations_table, unsafe_allow_html=True)
        else:
            st.write("No recommendations found. Please re-input")

# Run the Streamlit app
if __name__ == '__main__':
    app()

