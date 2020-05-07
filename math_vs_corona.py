import pandas as pd
import matplotlib.pyplot as plt

df_confirmed=pd.read_csv('./time_series_covid19_confirmed_global.csv')

indo = df_confirmed['Country/Region']=='Indonesia'
df_conf_indo=df_confirmed[indo]
df_conf_indo=df_conf_indo.drop(columns=['Province/State','Country/Region','Lat','Long'])
df_conf_indo=df_conf_indo.transpose()
df_conf_indo.columns=['indonesia']

plt.plot(df_conf_indo.indonesia)
plt.legend(['indonesia'],loc="upper left")
plt.xticks(rotation=90)
plt.figure(figsize=(10,5))
plt.show

malay = df_confirmed['Country/Region']=='Malaysia'
df_conf_malay=df_confirmed[malay]
df_conf_malay=df_conf_malay.drop(columns=['Province/State','Country/Region','Lat','Long'])
df_conf_malay=df_conf_malay.transpose()
df_conf_malay.columns=['malaysia']

singa = df_confirmed['Country/Region']=='Singapore'
df_conf_singa=df_confirmed[singa]
df_conf_singa=df_conf_singa.drop(columns=['Province/State','Country/Region','Lat','Long'])
df_conf_singa=df_conf_singa.transpose()
df_conf_singa.columns=['singapore']

thai = df_confirmed['Country/Region']=='Thailand'
df_conf_thai=df_confirmed[thai]
df_conf_thai=df_conf_thai.drop(columns=['Province/State','Country/Region','Lat','Long'])
df_conf_thai=df_conf_thai.transpose()
df_conf_thai.columns=['thailand']

philip = df_confirmed['Country/Region']=='Philippines'
df_conf_philip=df_confirmed[philip]
df_conf_philip=df_conf_philip.drop(columns=['Province/State','Country/Region','Lat','Long'])
df_conf_philip=df_conf_philip.transpose()
df_conf_philip.columns=['philippines']

viet = df_confirmed['Country/Region']=='Vietnam'
df_conf_viet=df_confirmed[viet]
df_conf_viet=df_conf_viet.drop(columns=['Province/State','Country/Region','Lat','Long'])
df_conf_viet=df_conf_viet.transpose()
df_conf_viet.columns=['vietnam']

cambo = df_confirmed['Country/Region']=='Cambodia'
df_conf_cambo=df_confirmed[cambo]
df_conf_cambo=df_conf_cambo.drop(columns=['Province/State','Country/Region','Lat','Long'])
df_conf_cambo=df_conf_cambo.transpose()
df_conf_cambo.columns=['cambodia']

laos = df_confirmed['Country/Region']=='Laos'
df_conf_laos=df_confirmed[laos]
df_conf_laos=df_conf_laos.drop(columns=['Province/State','Country/Region','Lat','Long'])
df_conf_laos=df_conf_laos.transpose()
df_conf_laos.columns=['laos']

brunei = df_confirmed['Country/Region']=='Brunei'
df_conf_brunei=df_confirmed[brunei]
df_conf_brunei=df_conf_brunei.drop(columns=['Province/State','Country/Region','Lat','Long'])
df_conf_brunei=df_conf_brunei.transpose()
df_conf_brunei.columns=['brunei']

df_asean=pd.concat([df_conf_indo, df_conf_malay, df_conf_singa, df_conf_thai, df_conf_philip, df_conf_viet, df_conf_cambo, df_conf_laos, df_conf_brunei], axis=1, sort=False)

plt.plot(df_asean)
plt.legend(['indonesia','malaysia','singapore','thailand','philippines','vietnam','cambodia','laos','brunei'],loc="upper left")
plt.xticks(rotation=90)
plt.figure(figsize=(10,5))
plt.show

df_death=pd.read_csv('./time_series_covid19_deaths_global.csv')

indo_d = df_death['Country/Region']=='Indonesia'
df_death_indo=df_death[indo_d]
df_death_indo=df_death_indo.drop(df_death_indo.columns[0:-1], axis=1)
df_death_indo=df_death_indo.transpose()
df_death_indo.columns=['indonesia']

malay_d = df_death['Country/Region']=='Malaysia'
df_death_malay=df_death[malay_d]
df_death_malay=df_death_malay.drop(df_death_malay.columns[0:-1], axis=1)
df_death_malay=df_death_malay.transpose()
df_death_malay.columns=['malaysia']

singa_d = df_death['Country/Region']=='Singapore'
df_death_singa=df_death[singa_d]
df_death_singa=df_death_singa.drop(df_death_singa.columns[0:-1], axis=1)
df_death_singa=df_death_singa.transpose()
df_death_singa.columns=['singapore']

thai_d = df_death['Country/Region']=='Thailand'
df_death_thai=df_death[thai_d]
df_death_thai=df_death_thai.drop(df_death_thai.columns[0:-1], axis=1)
df_death_thai=df_death_thai.transpose()
df_death_thai.columns=['thailand']

philip_d = df_death['Country/Region']=='Philippines'
df_death_philip=df_death[philip_d]
df_death_philip=df_death_philip.drop(df_death_philip.columns[0:-1], axis=1)
df_death_philip=df_death_philip.transpose()
df_death_philip.columns=['philippines']

viet_d = df_death['Country/Region']=='Vietnam'
df_death_viet=df_death[viet_d]
df_death_viet=df_death_viet.drop(df_death_viet.columns[0:-1], axis=1)
df_death_viet=df_death_viet.transpose()
df_death_viet.columns=['vietnam']

cambo_d = df_death['Country/Region']=='Cambodia'
df_death_cambo=df_death[cambo_d]
df_death_cambo=df_death_cambo.drop(df_death_cambo.columns[0:-1], axis=1)
df_death_cambo=df_death_cambo.transpose()
df_death_cambo.columns=['cambodia']

laos_d = df_death['Country/Region']=='Laos'
df_death_laos=df_death[laos_d]
df_death_laos=df_death_laos.drop(df_death_laos.columns[0:-1], axis=1)
df_death_laos=df_death_laos.transpose()
df_death_laos.columns=['laos']

brunei_d = df_death['Country/Region']=='Brunei'
df_death_brunei=df_death[brunei_d]
df_death_brunei=df_death_brunei.drop(df_death_brunei.columns[0:-1], axis=1)
df_death_brunei=df_death_brunei.transpose()
df_death_brunei.columns=['brunei']

df_asean_death=pd.concat([df_death_indo,df_death_malay,df_death_singa,df_death_thai,df_death_philip,df_death_viet,df_death_cambo,df_death_laos,df_death_brunei],axis=1, sort=False)

for i in range(len(df_asean.columns)):
    persentase_kematian =  df_asean_death.iloc[0,i]/df_asean.iloc[62,i] *100
    print("persentase kematian di {} adalah {}% dengan jumlah positif sebanyak {} dan korban meninggal sebanyak {}\n".format(df_asean.columns[i],persentase_kematian,df_asean.iloc[62,i],df_asean_death.iloc[0,i]))
    
positifindo=[686]
meninggalindo=[55]
sembuhindo=[30]
df_indo=pd.DataFrame(list(zip(positifindo,meninggalindo,sembuhindo)), columns=['positif','meninggal','sembuh'])

# The slices will be ordered and plotted counter-clockwise.
labels = 'Positif', 'Meninggal', 'Sembuh'
sizes = [601, 55, 30]
colors = ['yellow', 'red', 'green']
explode = (0, 0, 0)  # explode a slice if required

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True)
        
#draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.75,color='black', fc='white',linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)


# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.show()