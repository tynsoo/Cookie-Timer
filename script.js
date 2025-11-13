const cookieDough = document.getElementById('cookie-dough');
const cookieBaking = document.getElementById('cookie-baking');
const cookieDone = document.getElementById('cookie-done');  // Add this
const bakeStart = document.getElementById('bakeStart');
const bakeEnd = document.getElementById('bakeEnd');
const timerDisplay = document.getElementById('timer');
const doneMsg = document.getElementById('done');

// Timer variables
let timer = 600;
let intervalId = null;

// Helper: Format seconds as MM:SS
function formatTime(s) {
  const m = Math.floor(s / 60);
  const sec = s % 60;
  return `${m.toString().padStart(2, '0')}:${sec.toString().padStart(2, '0')}`;
}

// Start baking (countdown)
bakeStart.addEventListener('click', () => {
  if (intervalId !== null) return; 
  
  // Transition: show baking GIF, hide dough
  cookieDough.classList.add('hidden');
  cookieBaking.classList.remove('hidden');
  cookieDone.classList.add('hidden');
  doneMsg.classList.add('hidden');
  
  intervalId = setInterval(() => {
    timer--;
    timerDisplay.textContent = formatTime(timer);
    
    // When timer runs out
    if (timer <= 0) {
      clearInterval(intervalId);
      intervalId = null;
      
      // Hide baking, show done cookie
      cookieBaking.classList.add('hidden');
      cookieDone.classList.remove('hidden');  
      
      timerDisplay.classList.add('hidden');
      doneMsg.classList.remove('hidden');
    }
  }, 1000);
});

// Reset/stop baking
bakeEnd.addEventListener('click', resetTimer);

function resetTimer() {
  if (intervalId) {
    clearInterval(intervalId);
    intervalId = null;
  }
  
  timer = 600;
  timerDisplay.textContent = formatTime(timer);
  timerDisplay.classList.remove('hidden');
  doneMsg.classList.add('hidden');
  
 
  cookieDough.classList.remove('hidden');
  cookieBaking.classList.add('hidden');
  cookieDone.classList.add('hidden'); 
}

// Pre-load background image
const bgImg = new Image();
bgImg.src = '/images/background_2.png';

// Back button - go to start screen
document.getElementById('backBtn').addEventListener('click', () => {
    
    if (intervalId) {
      clearInterval(intervalId);
      intervalId = null;
    }
    
    window.location.href = 'index.html';
  });
