
// 📱💎⚡ Ultra dOoK Portal Service Worker ⚡💎📱
// ADHD-Optimized PWA with Offline Crystal Management

const CACHE_NAME = 'ultra-dook-portal-v1.0.0';
const STATIC_CACHE = 'static-cache-v1';
const DYNAMIC_CACHE = 'dynamic-cache-v1';

// Critical resources for ADHD optimization
const CRITICAL_RESOURCES = [
  '/',
  '/dashboard',
  '/create-crystal',
  '/agents',
  '/manifest.json',
  '/offline.html'
];

// Memory Crystal data patterns
const CRYSTAL_PATTERNS = [
  /\/api\/crystals/,
  /\/memory-crystals/,
  /\.json$/
];

// Install event - cache critical resources
self.addEventListener('install', event => {
  console.log('🚀 Ultra dOoK Service Worker installing...');
  
  event.waitUntil(
    caches.open(STATIC_CACHE)
      .then(cache => {
        console.log('💎 Caching critical resources for ADHD optimization');
        return cache.addAll(CRITICAL_RESOURCES);
      })
      .then(() => {
        console.log('✅ Critical resources cached - ADHD brain ready for offline mode');
        self.skipWaiting();
      })
  );
});

// Activate event - clean up old caches
self.addEventListener('activate', event => {
  console.log('🔗 Ultra dOoK Service Worker activating...');
  
  event.waitUntil(
    caches.keys()
      .then(cacheNames => {
        return Promise.all(
          cacheNames.map(cacheName => {
            if (cacheName !== STATIC_CACHE && cacheName !== DYNAMIC_CACHE) {
              console.log('🧹 Removing old cache:', cacheName);
              return caches.delete(cacheName);
            }
          })
        );
      })
      .then(() => {
        console.log('✅ Service Worker activated - Portal ready for legendary operation');
        self.clients.claim();
      })
  );
});

// Fetch event - enhanced caching strategy for ADHD needs
self.addEventListener('fetch', event => {
  const { request } = event;
  const url = new URL(request.url);
  
  // Handle Memory Crystal requests with special priority
  if (CRYSTAL_PATTERNS.some(pattern => pattern.test(url.pathname))) {
    event.respondWith(handleCrystalRequest(request));
    return;
  }
  
  // Handle navigation requests
  if (request.mode === 'navigate') {
    event.respondWith(handleNavigationRequest(request));
    return;
  }
  
  // Handle other requests with cache-first strategy
  event.respondWith(handleResourceRequest(request));
});

// Enhanced Memory Crystal handling for ADHD optimization
async function handleCrystalRequest(request) {
  try {
    // Always try network first for fresh crystal data
    const networkResponse = await fetch(request);
    
    if (networkResponse.ok) {
      // Cache successful crystal responses
      const cache = await caches.open(DYNAMIC_CACHE);
      cache.put(request, networkResponse.clone());
      
      console.log('💎 Fresh crystal data cached for offline access');
      return networkResponse;
    }
  } catch (error) {
    console.log('📱 Network unavailable, serving cached crystal data');
  }
  
  // Fallback to cached crystal data
  const cachedResponse = await caches.match(request);
  if (cachedResponse) {
    return cachedResponse;
  }
  
  // Ultimate fallback for crystals
  return new Response(JSON.stringify({
    error: 'Crystal data unavailable offline',
    message: 'Connect to network to sync latest crystals',
    offline: true
  }), {
    headers: { 'Content-Type': 'application/json' },
    status: 503
  });
}

// Navigation handling with ADHD-friendly offline experience
async function handleNavigationRequest(request) {
  try {
    // Try network first
    const networkResponse = await fetch(request);
    return networkResponse;
  } catch (error) {
    console.log('📱 Navigation offline, serving cached page');
    
    // Serve cached page or offline fallback
    const cachedResponse = await caches.match(request);
    if (cachedResponse) {
      return cachedResponse;
    }
    
    // Serve offline page with ADHD-friendly messaging
    return caches.match('/offline.html');
  }
}

// Resource request handling
async function handleResourceRequest(request) {
  // Cache-first strategy for static resources
  const cachedResponse = await caches.match(request);
  if (cachedResponse) {
    return cachedResponse;
  }
  
  try {
    const networkResponse = await fetch(request);
    
    // Cache successful responses
    if (networkResponse.ok) {
      const cache = await caches.open(DYNAMIC_CACHE);
      cache.put(request, networkResponse.clone());
    }
    
    return networkResponse;
  } catch (error) {
    console.log('📱 Resource unavailable offline:', request.url);
    
    // Return empty response for failed requests
    return new Response('', { status: 503 });
  }
}

// Background sync for Memory Crystals
self.addEventListener('sync', event => {
  console.log('🔄 Background sync triggered:', event.tag);
  
  if (event.tag === 'crystal-sync') {
    event.waitUntil(syncMemoryCrystals());
  }
  
  if (event.tag === 'agent-status-sync') {
    event.waitUntil(syncAgentStatus());
  }
});

// Sync memory crystals when back online
async function syncMemoryCrystals() {
  try {
    console.log('💎 Syncing memory crystals in background...');
    
    // Get pending crystal operations from IndexedDB
    const pendingCrystals = await getPendingCrystals();
    
    for (const crystal of pendingCrystals) {
      try {
        await fetch('/api/crystals', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(crystal)
        });
        
        // Remove from pending once synced
        await removePendingCrystal(crystal.id);
        console.log('✅ Crystal synced:', crystal.id);
      } catch (error) {
        console.log('❌ Failed to sync crystal:', crystal.id);
      }
    }
  } catch (error) {
    console.log('❌ Background crystal sync failed:', error);
  }
}

// Push notification handling for ADHD-friendly alerts
self.addEventListener('push', event => {
  console.log('🔔 Push notification received');
  
  let data = {};
  if (event.data) {
    data = event.data.json();
  }
  
  const options = {
    body: data.body || 'New update available in your empire!',
    icon: '/icons/icon-192x192.png',
    badge: '/icons/badge-72x72.png',
    tag: data.tag || 'default',
    requireInteraction: data.priority === 'high',
    silent: data.priority === 'low',
    actions: [
      {
        action: 'view',
        title: 'View Now',
        icon: '/icons/view-action.png'
      },
      {
        action: 'dismiss', 
        title: 'Later',
        icon: '/icons/dismiss-action.png'
      }
    ],
    data: data
  };
  
  event.waitUntil(
    self.registration.showNotification(
      data.title || 'Ultra dOoK Portal',
      options
    )
  );
});

// Notification click handling
self.addEventListener('notificationclick', event => {
  console.log('🔔 Notification clicked:', event.action);
  
  event.notification.close();
  
  if (event.action === 'view') {
    event.waitUntil(
      clients.openWindow(event.notification.data.url || '/')
    );
  }
});

// Helper functions for IndexedDB operations
async function getPendingCrystals() {
  // Implement IndexedDB read operation
  return [];
}

async function removePendingCrystal(crystalId) {
  // Implement IndexedDB delete operation
  console.log('🗑️ Removed pending crystal:', crystalId);
}

console.log('📱💎⚡ Ultra dOoK Portal Service Worker loaded - LEGENDARY PWA READY! ⚡💎📱');
