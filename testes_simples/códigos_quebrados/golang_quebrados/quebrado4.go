//Quebrado ainda
package main

import (
    "encoding/json"
    "net/http"
    "sync"
)

type Item struct {
    ID    string `json:"id"`
    Nome  string `json:"nome"`
    Valor int    `json:"valor"`
}

type Database struct {
    items map[string]Item
    mu    sync.RWMutex
}

func NewDatabase() *Database {
    return &Database{
        items: make(map[string]Item),
    }
}

func (db *Database) AddItem(item Item) {
    db.mu.Lock()
    defer db.mu.Unlock()
    db.items[item.ID] = item
}

func (db *Database) GetItem(id string) (Item, bool) {
    db.mu.RLock()
    defer db.mu.RUnlock()
    item, exists := db.items[id]
    return item, exists
}

func (db *Database) GetAllItems() []Item {
    db.mu.RLock()
    defer db.mu.RUnlock()
    items := make([]Item, 0, len(db.items))
    for _, item := range db.items {
        items = append(items, item)
    }
    return items
}

func main() {
    db := NewDatabase()
    
    http.HandleFunc("/items", func(w http.ResponseWriter, r *http.Request) {
        switch r.Method {
        case "GET":
            items := db.GetAllItems()
            json.NewEncoder(w).Encode(items)
        case "POST":
            var item Item
            if err := json.NewDecoder(r.Body).Decode(&item); err != nil {
                http.Error(w, err.Error(), http.StatusBadRequest)
                return
            }
            db.AddItem(item)
            w.WriteHeader(http.StatusCreated)
        default:
            http.Error(w, "Método não permitido", http.StatusMethodNotAllowed)
        }
    })

    http.ListenAndServe(":8080", nil)
}