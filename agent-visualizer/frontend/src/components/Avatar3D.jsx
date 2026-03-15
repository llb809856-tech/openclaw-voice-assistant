import React, { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { Sphere, Box, Cylinder, OrbitControls } from '@react-three/drei';
import * as THREE from 'three';

// 简单的 3D 机器人 Avatar
function RobotAvatar({ color = '#667eea', status = 'idle' }) {
  const groupRef = useRef();
  const headRef = useRef();
  
  // 动画
  useFrame((state) => {
    if (groupRef.current) {
      // 轻微浮动
      groupRef.current.position.y = Math.sin(state.clock.elapsedTime * 2) * 0.1;
      
      // 根据状态有不同的动画
      if (status === 'thinking') {
        // 思考时摇头
        groupRef.current.rotation.y = Math.sin(state.clock.elapsedTime) * 0.2;
      } else if (status === 'working') {
        // 工作时快速震动
        groupRef.current.position.x = Math.sin(state.clock.elapsedTime * 10) * 0.05;
      }
    }
    
    if (headRef.current) {
      // 头部跟随鼠标（轻微）
      headRef.current.rotation.y = Math.sin(state.clock.elapsedTime * 0.5) * 0.1;
    }
  });
  
  return (
    <group ref={groupRef}>
      {/* 身体 */}
      <Box args={[0.8, 1, 0.5]} position={[0, -0.5, 0]}>
        <meshStandardMaterial color={color} metalness={0.5} roughness={0.2} />
      </Box>
      
      {/* 头部 */}
      <group ref={headRef} position={[0, 0.3, 0]}>
        <Sphere args={[0.4, 32, 32]}>
          <meshStandardMaterial color={color} metalness={0.5} roughness={0.2} />
        </Sphere>
        
        {/* 眼睛 */}
        <Sphere args={[0.08, 16, 16]} position={[-0.15, 0.05, 0.35]}>
          <meshStandardMaterial color="#fff" emissive="#fff" emissiveIntensity={0.5} />
        </Sphere>
        <Sphere args={[0.08, 16, 16]} position={[0.15, 0.05, 0.35]}>
          <meshStandardMaterial color="#fff" emissive="#fff" emissiveIntensity={0.5} />
        </Sphere>
        
        {/* 嘴巴 - 根据状态变化 */}
        {status === 'idle' && (
          <Cylinder args={[0.02, 0.02, 0.15, 16]} position={[0, -0.15, 0.35]} rotation={[0, 0, 0]}>
            <meshStandardMaterial color="#fff" />
          </Cylinder>
        )}
        {status === 'thinking' && (
          <Sphere args={[0.05, 16, 16]} position={[0, -0.15, 0.35]}>
            <meshStandardMaterial color="#fff" />
          </Sphere>
        )}
        {status === 'working' && (
          <Cylinder args={[0.02, 0.02, 0.15, 16]} position={[0, -0.15, 0.35]} rotation={[0.5, 0, 0]}>
            <meshStandardMaterial color="#fff" />
          </Cylinder>
        )}
      </group>
      
      {/* 手臂 */}
      <Cylinder args={[0.1, 0.1, 0.6, 16]} position={[-0.6, -0.3, 0]} rotation={[0, 0, 0.3]}>
        <meshStandardMaterial color={color} metalness={0.5} roughness={0.2} />
      </Cylinder>
      <Cylinder args={[0.1, 0.1, 0.6, 16]} position={[0.6, -0.3, 0]} rotation={[0, 0, -0.3]}>
        <meshStandardMaterial color={color} metalness={0.5} roughness={0.2} />
      </Cylinder>
      
      {/* 腿 */}
      <Cylinder args={[0.12, 0.12, 0.7, 16]} position={[-0.25, -1.3, 0]}>
        <meshStandardMaterial color={color} metalness={0.5} roughness={0.2} />
      </Cylinder>
      <Cylinder args={[0.12, 0.12, 0.7, 16]} position={[0.25, -1.3, 0]}>
        <meshStandardMaterial color={color} metalness={0.5} roughness={0.2} />
      </Cylinder>
    </group>
  );
}

// 3D Avatar 展示组件
export default function Avatar3D({ agent }) {
  const statusColors = {
    idle: '#10b981',
    thinking: '#3b82f6',
    working: '#f59e0b',
    error: '#ef4444',
    offline: '#6b7280'
  };
  
  const color = statusColors[agent.status] || statusColors.idle;
  
  return (
    <div style={{ 
      width: '100%', 
      height: '200px',
      background: 'rgba(0,0,0,0.2)',
      borderRadius: '12px',
      overflow: 'hidden'
    }}>
      <Canvas camera={{ position: [0, 0, 3], fov: 50 }}>
        <ambientLight intensity={0.5} />
        <pointLight position={[10, 10, 10]} intensity={1} />
        <pointLight position={[-10, -10, -10]} intensity={0.5} />
        
        <RobotAvatar color={color} status={agent.status} />
        
        <OrbitControls 
          enableZoom={false}
          enablePan={false}
          autoRotate={true}
          autoRotateSpeed={2}
        />
      </Canvas>
    </div>
  );
}
