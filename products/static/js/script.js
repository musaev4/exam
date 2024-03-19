document.getElementById("main-image").onclick = function(){
    modal.style.display = "block";
    modalImg.src = this.src;
    captionText.innerHTML = this.alt;
  }

  var modal = document.getElementById("myModal");
  var modalImg = document.getElementById("img01");
  var captionText = document.getElementById("caption");
  var close = document.getElementsByClassName("close")[0];
  var images = document.querySelectorAll("#other-images img");
  var currentIndex = 0;

  close.onclick = function() {
    modal.style.display = "none";
  }

  // Обработчик клика по миниатюре изображения
  images.forEach(function(image, index) {
    image.onclick = function() {
      modal.style.display = "block";
      modalImg.src = this.src;
      captionText.innerHTML = this.alt;
      currentIndex = index;
    }
  });

  // Обработчики кликов по стрелкам
  document.querySelector('.prev').onclick = function() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    modalImg.src = images[currentIndex].src;
    captionText.innerHTML = images[currentIndex].alt;
  }

  document.querySelector('.next').onclick = function() {
    currentIndex = (currentIndex + 1) % images.length;
    modalImg.src = images[currentIndex].src;
    captionText.innerHTML = images[currentIndex].alt;
  }
