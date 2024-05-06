def unify(x,y,theta):
    if theta is None:
        return None
    elif x==y:
        return theta
    elif isinstance(x,int) and isinstance(y,int):
        return theta if x==y else None
    elif isinstance(x,list) and isinstance(y,list):
        if len(x)!=len(y):
            return None
        for i in range(len(x)):
            theta=unify(x[i],y[i],theta)
            if theta is None:
                return None
            return theta
    else:
        return None
    
theta=unify([1,3,4,5],[1,3,4,5],{})
if theta is None:
    print("Unification not possible")
else:
    print("Unification possible")