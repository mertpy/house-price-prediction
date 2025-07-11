import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


features = [
    'OverallQual','GrLivArea','GarageCars',
    'GarageArea','TotalBsmtSF','1stFlrSF',
    'YearBuilt','FullBath','TotRmsAbvGrd','Fireplaces'
]

df=pd.read_csv("train.csv")

y=df[["SalePrice"]]
x=df[features]

x_train, x_test, y_train, y_test=train_test_split(x,y,random_state=1, train_size=0.77)

l=LinearRegression()
model=l.fit(x_train,y_train)

train_score=model.score(x_train,y_train)
test_score=model.score(x_test,y_test)


plt.figure(figsize=(10,8))

for i, feature in enumerate(features):
    plt.subplot(4, 3, i+1)
    plt.scatter(x_test[[feature]], y_test, label="Real Price", alpha=0.6)
    plt.scatter(x_test[[feature]], model.predict(x_test), label="Predicted Price", alpha=0.6)
    plt.xlabel(feature)
    plt.ylabel("Price(real and predicted)")
    plt.title(f"{feature} vs Price")
    plt.legend()
    
plt.figtext(0.5, 0.01, f"Train score is %{round(train_score*100)}\n"
            f"Test score is %{round(test_score*100)}",
            ha='center', fontsize=16)
plt.tight_layout()
plt.show()



