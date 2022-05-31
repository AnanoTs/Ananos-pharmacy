from flask import render_template
@app.route('/')
def mainpagepharmacy():
    
    drugs_sort = drugs
    sort =  request.args.get("sort")
    if sort == "plh":
        for i in range(len(drugs_sort)):
            for o in range(len(drugs_sort)):
                if o<i and float(drugs_sort[o]["price"]) > float(drugs_sort[i]["price"]) :
                    y = drugs_sort[i]
                    drugs_sort[i] = drugs_sort[o]
                    drugs_sort[o] = y;
        
        return render_template("index.html", drugs_list=drugs_sort)

    elif sort == "phl":
        for i in range(len(drugs_sort)):
            for o in range(len(drugs_sort)):
                if o>i and float(drugs_sort[o]["price"]) > float(drugs_sort[i]["price"]) :
                    y = drugs_sort[i]
                    drugs_sort[i] = drugs_sort[o]
                    drugs_sort[o] = y;
        return render_template("index.html", drugs_list=drugs_sort)

    else:
        return render_template("index.html", drugs_list=drugs)