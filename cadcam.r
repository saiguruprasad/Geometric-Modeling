k <- 0;
options(digits=9)
x <- c(0,1);
z <- data.frame(NULL);
w <- c(0);
s.temp <- readline(prompt="Enter number of vertices: ")
n <- as.integer(s.temp)
s.temp <- readline(prompt="Enter slope of line: ")
m <- as.numeric(s.temp)
s.temp <- readline(prompt="Enter intercept of line: ")
c <- as.numeric(s.temp)
plot.new
m <- 0.5;
c <- 2;
x <- c(-10:10);
plot(x,m*x+c,type="l",col="blue")
axis(side =1, pos = c(0,0),lty="dotted")
axis(side =2, pos = c(0,0),lty="dotted")
j=1;
for (i in 1:n){
q <- locator(1,type = "p")
z[i,1] <- q$x
z[i,2] <- q$y
z[i,3] <- 1
}
#z <- data.frame(c(2,4,1),c(4,6,1),c(2,6,1));
#z <- t(z);
polygon(z[,1],z[,2],col="yellow")
z <- t(z);
slope <- -atan(m)
row1 <- c(cos(slope),sin(slope), 0);
row2 <- c(-sin(slope),cos(slope), 0);
row3 <- c(0,0,1);
matrixr <- data.frame(row1,row2,row3);
matrixt <- data.frame(c(1,0,0),c(0,1,0),c(0,-c,1));
matrixre <- data.frame(c(1,0,0),c(0,-1,0),c(0,0,1));
transform <- t(matrixt)%*%t(matrixr)%*%t(matrixre)%*%solve(t(matrixr))%*%solve(t(matrixt));
result <- t(z)%*%transform
polygon(result[,1],result[,2],col="magenta")
legend("topleft",legend=c("Real Points","Reflected Points","Reflection Line"),col= c("yellow","magenta","blue"),lty=c(0,0,1),lwd= c(0,0,1),pch= c(22,22,NA),pt.bg= c("yellow","magenta",NA),pt.cex=2,bty="n")
