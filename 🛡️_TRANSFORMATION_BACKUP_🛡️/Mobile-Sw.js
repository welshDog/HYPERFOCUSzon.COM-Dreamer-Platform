// Mobile Empire Command Center Service Worker
const CACHE_NAME = 'mobile-empire-v1.0.0';
const STATIC_CACHE = 'mobile-empire-static-v1.0.0';

// Cache strategy for different resource types
const CACHE_STRATEGIES = {
    documents: 'cache-first',
    scripts: 'cache-first',
    styles: 'cache-first',
    images: 'cache-first',
    api: 'network-first'
};

// Essential files to cache immediately
const ESSENTIAL_FILES = [
    './📱💎⚡_MOBILE_EMPIRE_COMMAND_CENTER_⚡💎📱.html',
    './mobile-manifest.json'
];

// Empire system endpoints for network-first caching
const EMPIRE_ENDPOINTS = [
    '/api/empire/status',
    '/api/portals/health',
    '/api/ai/crystals',
    '/api/analytics/realtime',
    '/api/deployment/queue'
];

// Install event - cache essential files
self.addEventListener('install', event => {
    console.log('📱 Mobile Empire Service Worker installing...');

    event.waitUntil(
        caches.open(STATIC_CACHE)
            .then(cache => {
                console.log('📱 Caching essential empire files...');
                return cache.addAll(ESSENTIAL_FILES);
            })
            .then(() => {
                console.log('📱 Mobile Empire Service Worker installed successfully!');
                return self.skipWaiting();
            })
            .catch(error => {
                console.error('📱 Service Worker installation failed:', error);
            })
    );
});

// Activate event - clean old caches
self.addEventListener('activate', event => {
    console.log('📱 Mobile Empire Service Worker activating...');

    event.waitUntil(
        caches.keys()
            .then(cacheNames => {
                return Promise.all(
                    cacheNames.map(cacheName => {
                        if (cacheName !== CACHE_NAME && cacheName !== STATIC_CACHE) {
                            console.log('📱 Removing old cache:', cacheName);
                            return caches.delete(cacheName);
                        }
                    })
                );
            })
            .then(() => {
                console.log('📱 Mobile Empire Service Worker activated!');
                return self.clients.claim();
            })
    );
});

// Fetch event - handle all network requests
self.addEventListener('fetch', event => {
    const { request } = event;
    const url = new URL(request.url);

    // Skip non-HTTP requests
    if (!url.protocol.startsWith('http')) {
        return;
    }

    // Determine cache strategy based on request type
    const strategy = getCacheStrategy(request);

    switch (strategy) {
        case 'cache-first':
            event.respondWith(cacheFirst(request));
            break;
        case 'network-first':
            event.respondWith(networkFirst(request));
            break;
        case 'stale-while-revalidate':
            event.respondWith(staleWhileRevalidate(request));
            break;
        default:
            event.respondWith(cacheFirst(request));
    }
});

// Cache-first strategy (for static assets)
async function cacheFirst(request) {
    try {
        const cachedResponse = await caches.match(request);
        if (cachedResponse) {
            return cachedResponse;
        }

        const networkResponse = await fetch(request);
        if (networkResponse.status === 200) {
            const cache = await caches.open(CACHE_NAME);
            cache.put(request, networkResponse.clone());
        }

        return networkResponse;
    } catch (error) {
        console.error('📱 Cache-first strategy failed:', error);
        return new Response('Empire system offline - cached version unavailable', {
            status: 503,
            statusText: 'Service Unavailable'
        });
    }
}

// Network-first strategy (for API calls)
async function networkFirst(request) {
    try {
        const networkResponse = await fetch(request);
        if (networkResponse.status === 200) {
            const cache = await caches.open(CACHE_NAME);
            cache.put(request, networkResponse.clone());
        }
        return networkResponse;
    } catch (error) {
        console.log('📱 Network failed, trying cache for:', request.url);
        const cachedResponse = await caches.match(request);

        if (cachedResponse) {
            return cachedResponse;
        }

        // Return offline response for empire systems
        return new Response(JSON.stringify({
            status: 'offline',
            message: 'Empire systems temporarily unavailable',
            cached: true,
            timestamp: Date.now()
        }), {
            status: 200,
            headers: { 'Content-Type': 'application/json' }
        });
    }
}

// Stale-while-revalidate strategy
async function staleWhileRevalidate(request) {
    const cache = await caches.open(CACHE_NAME);
    const cachedResponse = await cache.match(request);

    const fetchPromise = fetch(request).then(networkResponse => {
        if (networkResponse.status === 200) {
            cache.put(request, networkResponse.clone());
        }
        return networkResponse;
    }).catch(() => cachedResponse);

    return cachedResponse || fetchPromise;
}

// Determine cache strategy based on request
function getCacheStrategy(request) {
    const url = new URL(request.url);

    // Empire API endpoints - network first
    if (EMPIRE_ENDPOINTS.some(endpoint => url.pathname.includes(endpoint))) {
        return 'network-first';
    }

    // Static assets - cache first
    if (request.destination === 'document' ||
        request.destination === 'script' ||
        request.destination === 'style' ||
        request.destination === 'image') {
        return 'cache-first';
    }

    // Default to cache-first for mobile optimization
    return 'cache-first';
}

// Background sync for empire operations
self.addEventListener('sync', event => {
    if (event.tag === 'empire-sync') {
        console.log('📱 Empire background sync triggered');
        event.waitUntil(syncEmpireData());
    }
});

// Sync empire data when connection is restored
async function syncEmpireData() {
    try {
        // Sync with Memory Crystal Intelligence
        const crystalSync = fetch('/api/ai/crystals/sync', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                mobile: true,
                timestamp: Date.now(),
                patterns: 169
            })
        });

        // Sync portal status
        const portalSync = fetch('/api/portals/sync', {
            method: 'POST'
        });

        await Promise.all([crystalSync, portalSync]);
        console.log('📱 Empire data sync completed');

        // Notify all clients of successful sync
        const clients = await self.clients.matchAll();
        clients.forEach(client => {
            client.postMessage({
                type: 'EMPIRE_SYNC_COMPLETE',
                timestamp: Date.now()
            });
        });

    } catch (error) {
        console.error('📱 Empire sync failed:', error);
    }
}

// Push notifications for empire alerts
self.addEventListener('push', event => {
    if (!event.data) return;

    const data = event.data.json();
    const options = {
        body: data.body || 'Empire system notification',
        icon: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 192 192"><rect width="192" height="192" fill="%23667eea" rx="20"/><text x="96" y="130" font-size="100" text-anchor="middle" fill="white">📱</text></svg>',
        badge: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96"><rect width="96" height="96" fill="%23667eea"/><text x="48" y="65" font-size="50" text-anchor="middle" fill="white">⚡</text></svg>',
        tag: 'empire-notification',
        requireInteraction: true,
        vibrate: [200, 100, 200],
        actions: [
            {
                action: 'view',
                title: 'Open Command Center',
                icon: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" fill="%2300ff88"/><text x="24" y="32" font-size="24" text-anchor="middle" fill="white">👁️</text></svg>'
            },
            {
                action: 'dismiss',
                title: 'Dismiss',
                icon: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" fill="%23ff6b6b"/><text x="24" y="32" font-size="24" text-anchor="middle" fill="white">✕</text></svg>'
            }
        ]
    };

    event.waitUntil(
        self.registration.showNotification(
            data.title || '📱 Empire Command Alert',
            options
        )
    );
});

// Handle notification clicks
self.addEventListener('notificationclick', event => {
    event.notification.close();

    if (event.action === 'view') {
        event.waitUntil(
            clients.openWindow('./📱💎⚡_MOBILE_EMPIRE_COMMAND_CENTER_⚡💎📱.html')
        );
    }
});

// Periodic empire health check (when supported)
self.addEventListener('periodicsync', event => {
    if (event.tag === 'empire-health-check') {
        event.waitUntil(performEmpireHealthCheck());
    }
});

async function performEmpireHealthCheck() {
    try {
        const response = await fetch('/api/empire/health');
        const health = await response.json();

        if (health.status !== 'optimal') {
            await self.registration.showNotification('⚠️ Empire Health Alert', {
                body: `System status: ${health.status}. Immediate attention required.`,
                tag: 'empire-health',
                requireInteraction: true
            });
        }

        console.log('📱 Empire health check completed:', health.status);
    } catch (error) {
        console.error('📱 Empire health check failed:', error);
    }
}

console.log('📱💎⚡ MOBILE EMPIRE SERVICE WORKER LOADED ⚡💎📱');
