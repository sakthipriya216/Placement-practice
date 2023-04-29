//function as a parameter to other function

function add(a,b)
{
    return a+b;
}
function divide(a,b)
{
    return a/b;
}

function calculator(a,b,operator)
{
    return operator(a,b);   
}
