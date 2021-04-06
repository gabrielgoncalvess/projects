

library(ggplot2)
library(geobr)
library(raster)
library(fields)
library(ggspatial)

# definir diretório
setwd('C:/Users/gabre/Desktop/Projects/R/mapa_temperatura')
dados.temp <- read.csv('dados/dados_temperatura.csv')

relevo.mg <- raster('dados/relevo_minas_gerais.tif')
#plot(relevo.mg)

mg <- read_state(code_state = 'MG')
#plot(mg$geom)  # $ para pegar uma coluna específica

modelo <- lm(formula = temp~lon+lat+alt, data = dados.temp)  # ~ depende de

#summary(modelo)

relevo.df <- as.data.frame(relevo.mg, xy=TRUE)  # xy pegar a latitude e a longitude

relevo.df <- na.omit(relevo.df)  # omitir valores NA

names(relevo.df) <- c('lon', 'lat', 'alt')  # renomear colunas de um df

relevo.df$temp <- 23.49-0.25*relevo.df$lon+0.48*relevo.df$lat-0.0053*relevo.df$alt

relevo.df$temp2 <- predict(modelo, relevo.df)  # outra forma de fazer a de cima

ggplot(relevo.df)+
  geom_raster(aes(x=lon,y=lat,fill=temp))+
  geom_sf(data = mg, fill='NA')+
  scale_fill_gradientn(colours = tim.colors(10))+
  annotation_scale()+
  annotation_north_arrow(location='tl',
                         style = north_arrow_fancy_orienteering())+
  labs(x=NULL,y=NULL,fill='[°C]',title = 'Temperatura do ar')+
  theme_minimal()

ggsave(filename = 'temperatura.png')



