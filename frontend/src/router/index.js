import { createRouter, createWebHistory } from 'vue-router'
import ScheduleView from '@/views/ScheduleView.vue'
import HabitView from '@/views/HabitView.vue'
import TodoView from '@/views/TodoView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: TodoView
    },
    {
      path: '/schedule',
      name: 'schedule',
      component: ScheduleView,
    },
    {
      path: '/todo',
      name: 'todo',
      component: TodoView,
    },
    {
      path: '/habit',
      name: 'habit',
      component: HabitView,
    }
  ],
})

export default router
