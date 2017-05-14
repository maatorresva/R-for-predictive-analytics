#
M <- 150

x1 <- rnorm(M) * 0.5 - 0.1
x2 <- rnorm(M) * 0.5 - 0.2


y1 <- rnorm(M) * 0.4 + 3.2
y2 <- rnorm(M) * 0.5 

z1 <- rnorm(M) * 0.6
z2 <- rnorm(M) * 0.4 + 4.1

output <- c(rep(1, M), rep(2, M), rep(3, M))

d <- data.frame(x1 = c(x1, y1, z1),
                x2 = rnorm(3*M) * 0.3 + 2,
                x3 = runif(3*M) * 0.3 + 2,
                x4 = rnorm(3*M) * 0.1 - 3,
                x5 = c(x2, y2, z2) )
d$x6 = d$x1 * 0.2 + 3 + rnorm(3*M) * 0.05
d$x7 = d$x4 * 0.2 + 2 + rnorm(3*M) * 0.07
d$x8 = runif(3*M) * 0.1 + 10
d$x9 = runif(3*M) * 0.4 + 1
d$x10 = d$x6 + d$x7 + d$x1 + d$x5

d$class <- output

head(d)


write.table(d, 
            file = "datos.csv", 
            sep = ",", 
            dec = ".", 
            row.names = FALSE,
            col.names = TRUE)
