window.addEventListener('load', function() {
    this.setTimeout(function() {
        var tab1 = document.getElementById('tab-1');
        var tab2 = document.getElementById('tab-2');
        var container1 = document.getElementById('container-1');
        var container2 = document.getElementById('container-2');

        tab1.addEventListener('click', function() {
            container1.style.display = 'block';
            container2.style.display = 'none';
            tab1.classList.add('active');
            tab2.classList.remove('active');
        });

        tab2.addEventListener('click', function() {
            container1.style.display = 'none';
            container2.style.display = 'block';
            tab1.classList.remove('active');
            tab2.classList.add('active');
        });
    }, 2000);
});
