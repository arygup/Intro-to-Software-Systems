var i = 0;
var j = 0;
var data = ["Hello, I'm Aryan", "This is the type writer effect.", "Why am I studying ISS?"];
var rate = 60;
var flag = false;
function f() 
{
    if (flag == false) 
    {
        if (i < data[j].length) 
        {
            document.getElementById("para").innerHTML = document.getElementById("para").innerHTML + data[j].charAt(i);
            i++;
            setTimeout(f, rate);
            if (i == data[j].length) 
            {
                flag = true;
                console.log(flag);
            }
        }
    }
    else if (i > 0) {
        document.getElementById("para").innerHTML = data[j].substring(0, i);
        i--;
        setTimeout(f, rate);
        if (i == 0) 
        {
            flag = false;
            document.getElementById("para").innerHTML = "";
            j++;
            if (j > array.length - 1) 
            {
                j = 0;
            }
        }
    }
}