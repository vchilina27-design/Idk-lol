"use client"
import { Bell, Settings } from "lucide-react"
export function ProfileHeader({ name, role, tasksCompleted, totalTasks }: any) {
  const progressPct = totalTasks > 0 ? Math.round((tasksCompleted / totalTasks) * 100) : 0
  return (
    <div className="relative px-6 pt-12 pb-8 rounded-b-3xl overflow-hidden" style={{ background: "var(--header-bg)", color: "var(--header-fg)" }}>
      <div className="relative flex items-center justify-between mb-6">
        <div>
          <p className="text-white/70 text-xs font-medium tracking-wide uppercase">Welcome back</p>
          <p className="text-white font-bold text-lg leading-tight text-balance">{name}</p>
        </div>
      </div>
      <div className="relative rounded-2xl p-4" style={{ background: "rgba(255,255,255,0.15)" }}>
        <div className="flex items-center justify-between mb-2">
          <span className="text-white text-sm font-semibold">Daily Progress</span>
          <span className="text-white font-bold text-sm">{progressPct}%</span>
        </div>
      </div>
    </div>
  )
}
