from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from tasks.models import TodoItem, Category, PriorityCount
from collections import Counter


@receiver(m2m_changed, sender=TodoItem.category.through)
def task_cats_added(sender, instance, action, model, **kwargs):
    if action != "post_add":
        return

    for cat in instance.category.all():
        slug = cat.slug

        new_count = 0
        for task in TodoItem.objects.all():
            new_count += task.category.filter(slug=slug).count()

        Category.objects.filter(slug=slug).update(todos_count=new_count)


@receiver(m2m_changed, sender=TodoItem.category.through)
def task_cats_removed(sender, instance, action, model, **kwargs):
    if action != "post_remove":
        return

    cat_counter = Counter()
    for t in TodoItem.objects.all():
        for cat in t.category.all():
            cat_counter[cat.slug] += 1

    for slug, new_count in cat_counter.items():
        Category.objects.filter(slug=slug).update(todos_count=new_count)


@receiver(post_save, sender=TodoItem)
def new_task_added(sender, **kwargs):
    PriorityCount.objects.update_or_create(name='High Priority')
    PriorityCount.objects.update_or_create(name='Medium Priority')
    PriorityCount.objects.update_or_create(name='Low Priority')
    priorities = []
    priority_choices = {
        'High Priority': 0,
        'Medium Priority': 0,
        'Low Priority': 0,
    }
    for p in TodoItem.objects.all():
        priorities.append(p.priority)
    if priorities.count(1):
        priority_choices['High Priority'] = priorities.count(1)
    if priorities.count(2):
        priority_choices['Medium Priority'] = priorities.count(2)
    if priorities.count(3):
        priority_choices['Low Priority'] = priorities.count(3)
    for item, new_count in priority_choices.items():
        PriorityCount.objects.filter(name=item).update(
            todos_count=new_count)