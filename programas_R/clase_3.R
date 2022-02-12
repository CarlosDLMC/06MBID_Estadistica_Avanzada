# install.packages('MASS')
# install.packages('ISLR')
library(MASS)
library(ISLR)

set.seed(5)
train_ind = sample(seq_len(nrow(Boston)), size=floor(0.8 * nrow(Boston)))

train = Boston[train_ind, ]
test = Boston[-train_ind, ]

names(Boston)
lm.fit = lm(medv~lstat, data=train)

plot(c(1, 1, 1), c(1, 2, 3))
# plot(Boston[, names(Boston)])
plot(Boston[, c('crim', 'dis', 'chas')])

