import sys
sys.path.append('../')
from modules import * 
from paths import *
from columns import *

def pca_a(df,num_c):

    df_st = StandardScaler().fit_transform(df)

    pca=PCA(n_components=num_c).fit(df_st)
    pca_components = pca.components_

    

    pc_list = ["PC"+str(i) for i in list(range(1, num_c+1))]
    

    pca_components_df = pd.DataFrame.from_dict(dict(zip(pc_list, pca_components)))
    pca_components_df['polutant'] = df.columns.values

    pca_components_df = pca_components_df.set_index('polutant')

    

    plt.figure(figsize=(12, 6))
    explained_variance = (pca.explained_variance_ratio_)
    indx = np.arange(1,num_c+1, 1)

    print(df.shape)  # the original data
    print(pca.components_.shape)  # the principal components

    print('Length of indx:', len(indx))
    print('Length of explained_variance:', len(explained_variance))
    
    plt.bar(indx, explained_variance*100, alpha=0.5, align='center', label='Objašenjena varijanca za pojedinačne komponente', color = 'green')
    plt.plot(indx, np.cumsum(pca.explained_variance_ratio_)*100, 'g-o')
    plt.axhline(95, color='blue',  label = '95% objašnjene varijance')
    plt.ylabel('Omjer objašnjene varijance [%]')
    plt.xlabel('Glavne komponente')
    x = np.arange(1, pca_components_df.shape[1]+1, 1)
    plt.xticks(x, pc_list,rotation=20)
    plt.legend(loc='best')
    plt.title('')
    plt.grid()
    plt.tight_layout()
    return pca_components_df


def pca_3d(df):
    if df.shape[1]>3:
        df=df.reset_index()
        fig = px.scatter_3d(df, x='PC1', y='PC2', z='PC3',hover_name='polutant',color='col')

        # update figure layout
        fig.update_layout(autosize=False,width=800,height=800,)
        fig.show()

        
    
    else:
        df=df.reset_index()
        fig = px.scatter_3d(df, x='PC1', y='PC2', z='PC3',hover_name='polutant')

        # update figure layout
        fig.update_layout(
            autosize=False,
            width=800,
            height=800,
        )
        

        fig.show()
        
        
        
def kmeans_3d(df, broj_klastera):
    df = df.reset_index()
    
    # K-means clustering
    kmeans = KMeans(n_clusters=broj_klastera)
    klasteri = kmeans.fit_predict(df[['PC1','PC2','PC3']])
    df['Klaster'] = klasteri
    
    # Vizualizacija
    fig = px.scatter_3d(df, x='PC1', y='PC2', z='PC3', hover_name='polutant', color='Klaster')
    fig.update_layout(autosize=False, width=800, height=800)
    fig.show()
    
    return df

        
        
        
   