(() => {
  const header = document.querySelector(".site-header");
  const searchBtn = document.querySelector("[data-search]");
  const searchPanel = document.querySelector(".search-panel");
  const menuToggle = document.querySelector("[data-menu]");
  const mobileNav = document.querySelector(".mobile-nav");
  const toTop = document.querySelector(".to-top");

  const onScroll = () => {
    if (!header) return;
    header.classList.toggle("is-scrolled", window.scrollY > 40);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  searchBtn?.addEventListener("click", () => {
    searchPanel?.classList.toggle("open");
    searchPanel?.querySelector("input")?.focus();
  });
  const setMenu = (open) => {
    mobileNav?.classList.toggle("open", open);
    document.body.classList.toggle("menu-open", open);
    menuToggle?.setAttribute("aria-expanded", open ? "true" : "false");
    menuToggle?.setAttribute("aria-label", open ? "Close menu" : "Open menu");
  };
  menuToggle?.addEventListener("click", () => {
    setMenu(!mobileNav?.classList.contains("open"));
  });
  mobileNav?.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => setMenu(false));
  });
  window.addEventListener("resize", () => {
    if (window.innerWidth > 980) setMenu(false);
  });
  toTop?.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));

  const heroVideo = document.querySelector(".hero-video");
  const heroIframe = heroVideo?.querySelector("iframe");
  if (heroIframe) {
    const revealHero = () => heroVideo.classList.add("is-ready");
    const bindHero = () => {
      const player = new window.Vimeo.Player(heroIframe);
      player.setMuted(true).catch(() => {});
      player.setVolume(0).catch(() => {});
      player.on("playing", revealHero);
      player.on("bufferend", revealHero);
    };
    if (window.Vimeo) bindHero();
    else {
      const script = document.createElement("script");
      script.src = "https://player.vimeo.com/api/player.js";
      script.onload = bindHero;
      document.head.appendChild(script);
    }
    setTimeout(revealHero, 4000);
  }

  document.querySelectorAll(".nav-item").forEach((item) => {
    const btn = item.querySelector(":scope > button");
    btn?.addEventListener("click", (event) => {
      event.stopPropagation();
      document.querySelectorAll(".nav-item").forEach((other) => {
        if (other !== item) other.classList.remove("is-open");
      });
      item.classList.toggle("is-open");
    });
  });
  document.addEventListener("click", (event) => {
    if (event.target.closest(".nav-item")) return;
    document.querySelectorAll(".nav-item.is-open").forEach((item) => item.classList.remove("is-open"));
  });

  document.querySelectorAll("[data-form]").forEach((form) => {
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const note = form.parentElement.querySelector(".form-note") || form.querySelector(".form-note");
      note?.classList.add("show");
      form.reset();
    });
  });

  document.querySelectorAll("[data-day]").forEach((day) => {
    day.querySelectorAll("[data-tab]").forEach((tab) => {
      tab.addEventListener("click", () => {
        const target = tab.dataset.tab;
        day.querySelectorAll("[data-tab]").forEach((t) => t.classList.toggle("is-active", t === tab));
        day.querySelector("[data-panel='story']")?.classList.toggle("is-open", target === "story");
        day.querySelector("[data-panel='gallery']")?.classList.toggle("is-open", target === "gallery");
      });
    });
  });

  const lightbox = document.querySelector("[data-lightbox]");
  const lightboxImg = lightbox?.querySelector("img");
  document.querySelectorAll("[data-lightbox-src]").forEach((btn) => {
    btn.addEventListener("click", () => {
      if (!lightbox || !lightboxImg) return;
      lightboxImg.src = btn.dataset.lightboxSrc;
      lightboxImg.alt = btn.querySelector("img")?.alt || "";
      lightbox.hidden = false;
    });
  });
  lightbox?.querySelector("[data-lightbox-close]")?.addEventListener("click", () => {
    lightbox.hidden = true;
  });
  lightbox?.addEventListener("click", (event) => {
    if (event.target === lightbox) lightbox.hidden = true;
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && lightbox && !lightbox.hidden) lightbox.hidden = true;
  });

  const revealTargets = document.querySelectorAll(
    ".feature-row, .why-item, .blog-card, .partner, .day, .split-copy, .include-card, .swu-copy, .review-card, .itinerary-intro-grid > *, .partners-intro, .journey-card"
  );
  revealTargets.forEach((el) => el.classList.add("reveal"));
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("in");
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
  revealTargets.forEach((el) => io.observe(el));

  const filmstrips = document.querySelectorAll(".filmstrip");
  filmstrips.forEach((filmstrip) => {
    const originals = Array.from(filmstrip.children);
    originals.forEach((el) => filmstrip.appendChild(el.cloneNode(true)));

    const gap = parseFloat(getComputedStyle(filmstrip).columnGap || getComputedStyle(filmstrip).gap) || 10;
    const firstSetWidth = () => originals.reduce((sum, el) => sum + el.offsetWidth + gap, 0);

    let dragging = false;
    let paused = false;
    let startX = 0;
    let startScroll = 0;
    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    let offset = filmstrip.scrollLeft;
    const wrapScroll = () => {
      const loop = firstSetWidth();
      if (loop <= 0) return;
      if (offset >= loop) offset -= loop;
      if (offset < 0) offset += loop;
      filmstrip.scrollLeft = offset;
    };

    filmstrip.addEventListener("pointerdown", (event) => {
      dragging = true;
      paused = true;
      startX = event.clientX;
      startScroll = filmstrip.scrollLeft;
      offset = startScroll;
      filmstrip.setPointerCapture(event.pointerId);
    });
    filmstrip.addEventListener("pointermove", (event) => {
      if (!dragging) return;
      offset = startScroll - (event.clientX - startX);
      wrapScroll();
    });
    const stopDrag = () => {
      dragging = false;
      offset = filmstrip.scrollLeft;
      paused = filmstrip.matches(":hover");
    };
    filmstrip.addEventListener("pointerup", stopDrag);
    filmstrip.addEventListener("pointercancel", stopDrag);
    filmstrip.addEventListener("pointerenter", () => { paused = true; });
    filmstrip.addEventListener("pointerleave", () => { if (!dragging) paused = false; });

    if (!reduceMotion) {
      const tick = () => {
        if (!paused && !dragging) {
          offset += 0.3;
          wrapScroll();
        }
        requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    }
  });
})();
