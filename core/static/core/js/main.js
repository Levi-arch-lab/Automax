document.addEventListener("DOMContentLoaded", () => {
  const tabs = document.querySelectorAll(".tab");
  const groups = document.querySelectorAll(".services-group");

  tabs.forEach(tab => {
    tab.addEventListener("click", () => {

      tabs.forEach(t => t.classList.remove("active"));
      tab.classList.add("active");

      groups.forEach(g => g.classList.remove("active"));
      document.getElementById(tab.dataset.tab).classList.add("active");
    });
  });
});


// Animation
const elements = document.querySelectorAll('[data-animate]');

const observer = new IntersectionObserver((entries)=>{
    entries.forEach(entry=>{
        if(entry.isIntersecting){
            entry.target.classList.add('show');
        }
    });
},{
    threshold:0.2
});

elements.forEach(el=>{
    observer.observe(el);
});
