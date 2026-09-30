const CACHE_NAME = 'menu-signage-cache-v1';

// Fichiers à mettre en cache immédiatement (installation)
const PRECACHE_URLS = [
    '/',
    '/viewer.html',
    '/effects.js',
    'https://cdn.tailwindcss.com',
    'https://unpkg.com/vue@3/dist/vue.global.js',
    'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css'
];

self.addEventListener('install', event => {
    self.skipWaiting();
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            console.log('[Service Worker] Mise en cache des fichiers de base');
            return cache.addAll(PRECACHE_URLS).catch(err => console.log('Erreur precache:', err));
        })
    );
});

self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (cacheName !== CACHE_NAME) {
                        console.log('[Service Worker] Suppression de l\'ancien cache:', cacheName);
                        return caches.delete(cacheName);
                    }
                })
            );
        }).then(() => self.clients.claim())
    );
});

self.addEventListener('fetch', event => {
    const requestUrl = new URL(event.request.url);

    // Ignorer les requêtes non-GET (ex: POST, PUT) ou les requêtes vers d'autres protocoles (ex: chrome-extension)
    if (event.request.method !== 'GET' || !requestUrl.protocol.startsWith('http')) {
        return;
    }

    // Stratégie "Network First" pour le JSON de données (menu_data.json, etc.)
    // On veut toujours les dernières données si on a internet, sinon on prend le cache
    if (requestUrl.pathname.endsWith('.json') || requestUrl.pathname.includes('menu_data')) {
        event.respondWith(
            fetch(event.request)
                .then(response => {
                    // Sauvegarder dans le cache pour le mode hors ligne
                    const responseClone = response.clone();
                    caches.open(CACHE_NAME).then(cache => cache.put(event.request, responseClone));
                    return response;
                })
                .catch(() => {
                    console.log('[Service Worker] Hors ligne, utilisation du JSON en cache');
                    return caches.match(event.request);
                })
        );
        return;
    }

    // Stratégie "Cache First, puis Network" pour les images, vidéos, polices, scripts
    event.respondWith(
        caches.match(event.request).then(cachedResponse => {
            if (cachedResponse) {
                // Optionnel: Mettre à jour le cache en arrière-plan (Stale-While-Revalidate)
                // fetch(event.request).then(response => {
                //     caches.open(CACHE_NAME).then(cache => cache.put(event.request, response));
                // }).catch(() => {});
                return cachedResponse;
            }

            // Si pas dans le cache, on télécharge et on met en cache
            return fetch(event.request).then(response => {
                // Ne pas mettre en cache si la réponse n'est pas OK
                if (!response || response.status !== 200 || response.type !== 'basic') {
                    if(response.type === 'cors' || response.type === 'opaque') {
                        // On cache quand même les requêtes cross-origin (CDN)
                        const responseClone = response.clone();
                        caches.open(CACHE_NAME).then(cache => cache.put(event.request, responseClone));
                    }
                    return response;
                }

                const responseClone = response.clone();
                caches.open(CACHE_NAME).then(cache => {
                    cache.put(event.request, responseClone);
                });

                return response;
            }).catch(() => {
                console.log('[Service Worker] Échec réseau pour:', event.request.url);
                // Gérer l'erreur réseau si besoin (ex: image par défaut)
            });
        })
    );
});
