#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template


# In[2]:


app = Flask(__name__)


# In[3]:


import joblib


# In[4]:


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        purchases = request.form.get("purchases")
        suppcard = request.form.get("suppcard")
        print(purchases, suppcard)
        model1 = joblib.load("CART")
        model2 = joblib.load("CART")
        model3 = joblib.load("CART")
        pred1 = model1.predict([[int(purchases), int(suppcard)]])
       
        pred2 = model2.predict([[int(purchases), int(suppcard)]])
       
        pred3 = model3.predict([[int(purchases), int(suppcard)]])
        
     
        return(render_template("index.html", result1=pred1, result2=pred2, result3=pred3))
    else:
        return(render_template("index.html", result1="2", result2="2",result3="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




