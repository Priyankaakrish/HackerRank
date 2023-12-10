function Rectangle(a, b) {
    var perimeter = 2*(a+b);
    var area = a*b;
    var length = a;
    var width = b;
    var rec = {length, width, perimeter, area};
    return rec;
}