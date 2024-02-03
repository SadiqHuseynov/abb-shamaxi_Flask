//KreditHesablama______________________________________
function krediHesapla() {
    const krediMiktariAZN = parseFloat(document.getElementById("krediMiktari").value);
    const faizOrani = parseFloat(document.getElementById("faizOrani").value) / 100;
    const vadeSuresi = parseInt(document.getElementById("vadeSuresi").value);

    const aylikFaizOrani = faizOrani / 12;
    const aylikTaksitAZN = (krediMiktariAZN * aylikFaizOrani) / (1 - Math.pow(1 + aylikFaizOrani, -vadeSuresi));
    const toplamOdemeAZN = aylikTaksitAZN * vadeSuresi;

    document.getElementById("aylikOdeme").textContent = aylikTaksitAZN.toFixed(2) + " ₼";
    document.getElementById("toplamOdeme").textContent = toplamOdemeAZN.toFixed(2) + " ₼";
}

// Kredi miktarı, faiz oranı ve kredi süresi aralıklarının değerlerini göster
document.getElementById("krediMiktari").addEventListener("input", function () {
    document.getElementById("krediMiktariGoster").textContent = this.value + " AZN";
    krediHesapla(); // Kredi miktarı değiştiğinde hesaplamayı güncelle
});

document.getElementById("faizOrani").addEventListener("input", function () {
    document.getElementById("faizOraniGoster").textContent = this.value + "%";
    krediHesapla(); // Faiz oranı değiştiğinde hesaplamayı güncelle
});

document.getElementById("vadeSuresi").addEventListener("input", function () {
    document.getElementById("vadeSuresiGoster").textContent = this.value + " Ay";
    krediHesapla(); // Kredi süresi değiştiğinde hesaplamayı güncelle
});  
//Modal______________________________________
function openModalAfterDelay() {
    $('#exampleModal').modal('show');
  }

  setTimeout(openModalAfterDelay, 5000);

  $('#openModalButton').click(function() {
    clearTimeout(openModalAfterDelay);
  });
