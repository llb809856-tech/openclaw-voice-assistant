/**
 * 声音管理器
 * 播放各种提示音和音效
 */

class SoundManager {
  constructor() {
    this.sounds = {};
    this.enabled = true;
    this.volume = 0.5;
    
    // 预加载音效
    this.preloadSounds();
  }
  
  /**
   * 预加载系统音效
   */
  preloadSounds() {
    // macOS 系统音效路径
    const systemSounds = {
      glass: '/System/Library/Sounds/Glass.aiff',      // 任务完成
      ping: '/System/Library/Sounds/Ping.aiff',        // 提醒
      basso: '/System/Library/Sounds/Basso.aiff',      // 错误
      hero: '/System/Library/Sounds/Hero.aiff',        // 成就解锁
      morse: '/System/Library/Sounds/Morse.aiff',      // 消息
      submarine: '/System/Library/Sounds/Submarine.aiff', // 警告
      sosumi: '/System/Library/Sounds/Sosumi.aiff',    // 通知
      pop: '/System/Library/Sounds/Pop.aiff'           // 弹窗
    };
    
    // 创建 Audio 对象
    for (const [name, path] of Object.entries(systemSounds)) {
      const audio = new Audio();
      audio.src = path;
      audio.volume = this.volume;
      this.sounds[name] = audio;
    }
    
    // 自定义音效（使用 Web Audio API 生成）
    this.createCustomSounds();
  }
  
  /**
   * 创建自定义音效
   */
  createCustomSounds() {
    // 使用 AudioContext 生成简单音效
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    
    // 升级音效
    this.sounds.levelUp = {
      play: () => {
        const oscillator = audioContext.createOscillator();
        const gainNode = audioContext.createGain();
        
        oscillator.connect(gainNode);
        gainNode.connect(audioContext.destination);
        
        oscillator.frequency.setValueAtTime(523.25, audioContext.currentTime); // C5
        oscillator.frequency.setValueAtTime(659.25, audioContext.currentTime + 0.1); // E5
        oscillator.frequency.setValueAtTime(783.99, audioContext.currentTime + 0.2); // G5
        oscillator.frequency.setValueAtTime(1046.50, audioContext.currentTime + 0.3); // C6
        
        gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.5);
        
        oscillator.start(audioContext.currentTime);
        oscillator.stop(audioContext.currentTime + 0.5);
      }
    };
    
    // Token 消耗音效
    this.sounds.tokenSpend = {
      play: () => {
        const oscillator = audioContext.createOscillator();
        const gainNode = audioContext.createGain();
        
        oscillator.connect(gainNode);
        gainNode.connect(audioContext.destination);
        
        oscillator.type = 'sine';
        oscillator.frequency.setValueAtTime(880, audioContext.currentTime);
        oscillator.frequency.exponentialRampToValueAtTime(440, audioContext.currentTime + 0.1);
        
        gainNode.gain.setValueAtTime(0.1, audioContext.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.1);
        
        oscillator.start(audioContext.currentTime);
        oscillator.stop(audioContext.currentTime + 0.1);
      }
    };
    
    // 低 Token 预警音效
    this.sounds.lowToken = {
      play: () => {
        const oscillator = audioContext.createOscillator();
        const gainNode = audioContext.createGain();
        
        oscillator.connect(gainNode);
        gainNode.connect(audioContext.destination);
        
        oscillator.type = 'triangle';
        oscillator.frequency.setValueAtTime(440, audioContext.currentTime);
        oscillator.frequency.setValueAtTime(440, audioContext.currentTime + 0.1);
        oscillator.frequency.setValueAtTime(440, audioContext.currentTime + 0.2);
        
        gainNode.gain.setValueAtTime(0.2, audioContext.currentTime);
        gainNode.gain.setValueAtTime(0.2, audioContext.currentTime + 0.1);
        gainNode.gain.setValueAtTime(0.2, audioContext.currentTime + 0.2);
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.4);
        
        oscillator.start(audioContext.currentTime);
        oscillator.stop(audioContext.currentTime + 0.4);
      }
    };
  }
  
  /**
   * 播放音效
   */
  play(soundName) {
    if (!this.enabled) return;
    
    const sound = this.sounds[soundName];
    if (sound) {
      try {
        // 重置到开头
        sound.currentTime = 0;
        sound.play().catch(err => {
          console.warn(`Failed to play sound ${soundName}:`, err);
        });
      } catch (err) {
        console.warn(`Failed to play sound ${soundName}:`, err);
      }
    }
  }
  
  /**
   * 任务完成音效
   */
  playTaskComplete() {
    this.play('glass');
  }
  
  /**
   * 成就解锁音效
   */
  playAchievement() {
    this.play('hero');
    setTimeout(() => this.play('levelUp'), 300);
  }
  
  /**
   * 升级音效
   */
  playLevelUp() {
    this.play('levelUp');
  }
  
  /**
   * 错误音效
   */
  playError() {
    this.play('basso');
  }
  
  /**
   * 警告音效
   */
  playWarning() {
    this.play('submarine');
  }
  
  /**
   * Token 消耗音效
   */
  playTokenSpend() {
    this.play('tokenSpend');
  }
  
  /**
   * 低 Token 预警音效
   */
  playLowToken() {
    this.play('lowToken');
  }
  
  /**
   * 消息提示音效
   */
  playMessage() {
    this.play('morse');
  }
  
  /**
   * 设置音量
   */
  setVolume(volume) {
    this.volume = Math.max(0, Math.min(1, volume));
    for (const sound of Object.values(this.sounds)) {
      if (sound.volume !== undefined) {
        sound.volume = this.volume;
      }
    }
  }
  
  /**
   * 启用/禁用音效
   */
  setEnabled(enabled) {
    this.enabled = enabled;
  }
}

// 导出单例
export const soundManager = new SoundManager();
export default soundManager;
