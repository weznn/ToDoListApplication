import json
import os


def load_tasks(filename="tasks.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []


def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(task, filename="tasks.json"):
    tasks = load_tasks(filename)
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks, filename)
    print("Görev eklendi!")


def list_tasks(filename="tasks.json"):
    tasks = load_tasks(filename)
    if not tasks:
        print("Henüz görev yok!")
    for i, task in enumerate(tasks, 1):
        status = "[X]" if task["completed"] else "[ ]"
        print(f"{i}. {status} {task['task']}")


def complete_task(index, filename="tasks.json"):
    tasks = load_tasks(filename)
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks, filename)
        print("Görev tamamlandı!")
    else:
        print("Geçersiz görev numarası!")


def delete_task(index, filename="tasks.json"):
    tasks = load_tasks(filename)
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks, filename)
        print("Görev silindi!")
    else:
        print("Geçersiz görev numarası!")


def main():
    while True:
        print("\n1. Görev ekle")
        print("2. Görevleri listele")
        print("3. Görevi tamamla")
        print("4. Görevi sil")
        print("5. Çıkış")

        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            task = input("Görev açıklamasını girin: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            index = int(input("Tamamlamak istediğiniz görevin numarasını girin: ")) - 1
            complete_task(index)
        elif choice == "4":
            index = int(input("Silmek istediğiniz görevin numarasını girin: ")) - 1
            delete_task(index)
        elif choice == "5":
            break
        else:
            print("Geçersiz seçim, tekrar deneyin!")


if __name__ == "__main__":
    main()
