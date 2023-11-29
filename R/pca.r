# Učitavanje potrebnih paketa
library(ggplot2)
library(dplyr)
library(httpgd)
library(plotly)

# Učitavanje podataka
podaci <- read.csv("/home/ivana/repozitorij/diplomski/ivana_dip/data/PAH_PCB_OCP.csv") # nolint: line_length_linter.
data <- podaci[, -c(1, 2, 3, 4, 5, 6, 39, 42)]

# Standardiziranje podataka
# Pretpostavljamo da su sve varijable (stupci) relevantni za analizu
podaci_scaled <- scale(data)

# Izvođenje PCA
pca_result <- prcomp(podaci_scaled, center = TRUE, scale. = TRUE)

# Analiza rezultata
# Prikazuje koliko svaka komponenta doprinosi ukupnoj varijanci
summary(pca_result)

# Vizualizacija rezultata - Prve dvije glavne komponente
pca_data <- as.data.frame(pca_result$x)
my_plot <- plot_ly(data = pca_data, x = ~PC1, y = ~PC2, z = ~PC3, type = "scatter3d", mode = "markers") %>% # nolint: line_length_linter.
  layout(scene = list(xaxis = list(title = "Prva glavna komponenta"),
                      yaxis = list(title = "Druga glavna komponenta"),
                      zaxis = list(title = "Treća glavna komponenta")),
         title = "PCA analiza u 3D")


plotly::export(my_plot, file = "my_plot.png", format = "png")
