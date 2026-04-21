(() => {
  const scene = document.getElementById("scene");
  const portalFrame = document.getElementById("portalFrame");
  const guard = document.getElementById("guard");
  const attemptButton = document.getElementById("attemptButton");
  const statusPill = document.getElementById("statusPill");
  const urlDisplay = document.getElementById("urlDisplay");
  const flagDisplay = document.getElementById("flagDisplay");
  const flagValue = document.getElementById("flagValue");
  const copyFlagButton = document.getElementById("copyFlagButton");
  const copyFeedback = document.getElementById("copyFeedback");

  const modal = document.getElementById("guardModal");
  const closeModalButton = document.getElementById("closeModal");
  const cardName = document.getElementById("cardName");
  const cardStatus = document.getElementById("cardStatus");
  const guardMessage = document.getElementById("guardMessage");

  const particleField = document.getElementById("particleField");

  let hasWon = false;

  function ensureStatusParameter() {
    const currentUrl = new URL(window.location.href);
    const rawStatus = (currentUrl.searchParams.get("status") || "").trim();

    if (!rawStatus) {
      currentUrl.searchParams.set("status", "normal");
      window.history.replaceState({}, "", currentUrl.toString());
      return "normal";
    }

    return rawStatus;
  }

  const enteredStatus = ensureStatusParameter();
  const normalizedStatus = enteredStatus.toLowerCase();

  function toCardStatus(value) {
    if (value === "vip") {
      return "VIP User";
    }

    if (value === "normal") {
      return "Normal User";
    }

    return `Unrecognized: ${enteredStatus}`;
  }

  function toPillStatus() {
    if (normalizedStatus === "vip") {
      return "Scanner Status: VIP USER";
    }

    if (normalizedStatus === "normal") {
      return "Scanner Status: NORMAL USER";
    }

    const shortStatus =
      enteredStatus.length > 20
        ? `${enteredStatus.slice(0, 20)}...`
        : enteredStatus;

    return `Scanner Status: ${shortStatus.toUpperCase()} - INVALID FOR GATE`;
  }

  function deniedMessage() {
    if (normalizedStatus === "normal") {
      return "Hold it. My scanner shows you are a 'Normal User'. Access denied. Hint: this gate validates URL query tokens, not identity titles.";
    }

    if (normalizedStatus === "admin") {
      return "Nice try. Your card says 'admin', but this gateway ignores grand role names. Think of a shorter elite tier token.";
    }

    return `Denied. Your scanner value is '${enteredStatus}'. This token is not accepted by the gate core. Hint: inspect and manipulate the URL query value.`;
  }

  async function fetchFlag() {
    try {
      const response = await fetch(
        `/api/flag?status=${encodeURIComponent(enteredStatus)}`,
      );

      if (!response.ok) {
        return "[decryption failed]";
      }

      const data = await response.json();
      if (!data.flag) {
        return "[flag unavailable]";
      }

      return data.flag;
    } catch {
      return "[connection error while retrieving flag]";
    }
  }

  async function copyFlagText() {
    const text = flagValue.textContent.trim();
    if (!text || text.startsWith("[") || text === "Decrypting payload...") {
      copyFeedback.textContent = "No flag yet";
      return;
    }

    try {
      await navigator.clipboard.writeText(text);
      copyFeedback.textContent = "Copied";
    } catch {
      const range = document.createRange();
      range.selectNodeContents(flagValue);
      const selection = window.getSelection();
      if (selection) {
        selection.removeAllRanges();
        selection.addRange(range);
      }

      try {
        const ok = document.execCommand("copy");
        copyFeedback.textContent = ok ? "Copied" : "Select and copy";
      } finally {
        if (selection) {
          selection.removeAllRanges();
        }
      }
    }

    window.setTimeout(() => {
      copyFeedback.textContent = "";
    }, 1200);
  }

  function updateUrlReadout() {
    urlDisplay.textContent = window.location.href;

    if (normalizedStatus === "vip") {
      statusPill.textContent = toPillStatus();
      statusPill.classList.add("vip");
      statusPill.classList.remove("invalid");
      scene.classList.add("victory-ready");
    } else if (normalizedStatus === "normal") {
      statusPill.textContent = toPillStatus();
      statusPill.classList.remove("vip", "invalid");
      scene.classList.remove("victory-ready");
    } else {
      statusPill.textContent = toPillStatus();
      statusPill.classList.remove("vip");
      statusPill.classList.add("invalid");
      scene.classList.remove("victory-ready");
    }
  }

  function createParticles() {
    const particleCount = 30;

    for (let i = 0; i < particleCount; i += 1) {
      const particle = document.createElement("span");
      const size = Math.random() * 4 + 1;
      const duration = Math.random() * 12 + 10;
      const delay = Math.random() * -duration;

      particle.className = "particle";
      particle.style.left = `${Math.random() * 100}%`;
      particle.style.top = `${Math.random() * 110}%`;
      particle.style.width = `${size}px`;
      particle.style.height = `${size}px`;
      particle.style.animationDuration = `${duration}s`;
      particle.style.animationDelay = `${delay}s`;

      particleField.appendChild(particle);
    }
  }

  function showModal() {
    modal.classList.add("is-visible");
    modal.setAttribute("aria-hidden", "false");
    closeModalButton.focus();
  }

  function hideModal() {
    modal.classList.remove("is-visible");
    modal.setAttribute("aria-hidden", "true");
  }

  function runDeniedFlow() {
    guard.classList.remove("is-saluting", "is-aside");
    guard.classList.add("is-blocking");
    attemptButton.classList.add("denied-pulse");

    cardName.textContent = "Guest";
    cardStatus.textContent = toCardStatus(normalizedStatus);
    guardMessage.textContent = deniedMessage();

    showModal();

    window.setTimeout(() => {
      guard.classList.remove("is-blocking");
      attemptButton.classList.remove("denied-pulse");
    }, 900);
  }

  function runVipFlow() {
    if (hasWon) {
      return;
    }

    hideModal();
    guard.classList.remove("is-blocking");
    guard.classList.add("is-saluting");

    window.setTimeout(() => {
      guard.classList.add("is-aside");
    }, 240);

    portalFrame.classList.add("is-opening");

    window.setTimeout(() => {
      portalFrame.classList.add("is-open");
    }, 680);

    window.setTimeout(async () => {
      scene.classList.add("victory");
      flagValue.textContent = "Decrypting payload...";
      flagDisplay.classList.add("visible");
      statusPill.textContent = "Scanner Status: VIP USER - ACCESS CONFIRMED";
      statusPill.classList.add("vip");
      attemptButton.textContent = "VIP Access Granted";
      attemptButton.disabled = true;
      attemptButton.classList.add("is-hidden");

      const resolvedFlag = await fetchFlag();
      flagValue.textContent = resolvedFlag;

      hasWon = true;
    }, 1400);
  }

  attemptButton.addEventListener("click", () => {
    if (normalizedStatus === "vip") {
      runVipFlow();
      return;
    }

    runDeniedFlow();
  });

  closeModalButton.addEventListener("click", hideModal);

  modal.addEventListener("click", (event) => {
    if (event.target === modal) {
      hideModal();
    }
  });

  copyFlagButton.addEventListener("click", copyFlagText);

  window.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      hideModal();
    }
  });

  createParticles();
  updateUrlReadout();
})();
