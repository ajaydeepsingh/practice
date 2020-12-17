var calc = function () {
    var bill = document.getElementById("bill").value;
    var totalPeople = document.getElementById("totalPeople").value;
    var tip = document.getElementById("tip").value;

    var tipTotal = (tip / 100);

    var userportionoftip = (bill * tipTotal) / totalPeople;
    var userportionofbill = (bill / totalPeople)
    total = Math.round(userportionoftip + userportionofbill);
    total = total.toFixed(2);

    document.getElementById("tipres").innerHTML = "$" + Number(bill * tipTotal).toFixed(2);
    document.getElementById("total").innerHTML = "$" + Number(bill*(1+tipTotal)).toFixed(2);
    document.getElementById("splitTotal").innerHTML = "$" + Number((bill*(1+tipTotal))/totalPeople).toFixed(2);
};
