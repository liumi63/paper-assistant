const STORAGE_KEY = 'paper-assistant:user'

export function saveUser(user) {
  if (!user) return
  localStorage.setItem(STORAGE_KEY, JSON.stringify(user))
  window.dispatchEvent(new CustomEvent('auth-changed'))
}

export function saveSessionUser(user) {
  if (!user) return
  sessionStorage.setItem(STORAGE_KEY, JSON.stringify(user))
  window.dispatchEvent(new CustomEvent('auth-changed'))
}

export function loadUser() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY) ?? sessionStorage.getItem(STORAGE_KEY)
    return raw ? JSON.parse(raw) : null
  } catch (error) {
    console.warn('Failed to parse user from localStorage', error)
    return null
  }
}

export function clearUser() {
  localStorage.removeItem(STORAGE_KEY)
  sessionStorage.removeItem(STORAGE_KEY)
  window.dispatchEvent(new CustomEvent('auth-changed'))
}

export function isLoggedIn() {
  return Boolean(loadUser())
}
