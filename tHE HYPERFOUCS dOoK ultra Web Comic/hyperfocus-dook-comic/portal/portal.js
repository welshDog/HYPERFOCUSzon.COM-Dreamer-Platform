// --- HYPER dOoK Portal JS ---

// Mock data for demo (replace with real data source later)
const chapters = [
    { title: 'Welcome to the Ultra dOoK', author: 'BROSKI♾️', date: '2025-07-25', type: 'chapter', secret: false },
    { title: 'Our Legendary Chapter', author: 'HYPER TEAM', date: '2025-07-26', type: 'chapter', secret: false },
    { title: 'Secret Memory #1', author: 'BROSKI♾️', date: '2025-07-26', type: 'memory', secret: true },
    { title: 'Team Easter Egg', author: 'HYPER TEAM', date: '2025-07-26', type: 'memory', secret: true }
];

const team = [
    'BROSKI♾️', 'ARIA', 'CHARLIE', 'ALEX', 'MORGAN', 'SAGE', 'PHOENIX', 'RUBY'
];

let dopamine = 0;

function updateStats() {
    document.getElementById('chapterCount').textContent = `Chapters: ${chapters.filter(c => c.type === 'chapter').length}`;
    document.getElementById('teamCount').textContent = `Team: ${team.length}`;
    document.getElementById('dopamineBar').value = dopamine;
}

function renderTimeline() {
    const timeline = document.getElementById('crystalTimeline');
    timeline.innerHTML = '';
    chapters.forEach((c, i) => {
        const crystal = document.createElement('div');
        crystal.className = 'crystal';
        crystal.title = `${c.title} by ${c.author} (${c.date})`;
        crystal.innerHTML = c.secret ? '🔮' : '💎';
        crystal.onclick = () => showCrystalInfo(c);
        timeline.appendChild(crystal);
    });
}

function showCrystalInfo(c) {
    let msg = `${c.title}\nBy: ${c.author}\nDate: ${c.date}`;
    if (c.secret) msg += '\n[Secret Memory Unlocked!]';
    alert(msg);
}

function celebrate() {
    dopamine = Math.min(100, dopamine + 20);
    updateStats();
    launchConfetti();
    showCelebrationGif();
}

function launchConfetti() {
    const confettiDiv = document.getElementById('confetti');
    confettiDiv.innerHTML = '';
    for (let i = 0; i < 40; i++) {
        const conf = document.createElement('span');
        conf.textContent = '🎊';
        conf.style.fontSize = `${Math.random() * 1.5 + 1}rem`;
        conf.style.position = 'relative';
        conf.style.left = `${Math.random() * 90}%`;
        confettiDiv.appendChild(conf);
    }
    setTimeout(() => { confettiDiv.innerHTML = ''; }, 2000);
}

function showCelebrationGif() {
    const gifs = [
        'https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif',
        'https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif',
        'https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif',
        'https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif'
    ];
    const gifDiv = document.getElementById('celebrationGif');
    gifDiv.innerHTML = `<img src="${gifs[Math.floor(Math.random() * gifs.length)]}" alt="Celebration!" />`;
    setTimeout(() => { gifDiv.innerHTML = ''; }, 3500);
}

document.getElementById('celebrateBtn').onclick = celebrate;

// Init
updateStats();
renderTimeline();
