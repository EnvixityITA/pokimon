<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Panzer III WWII - Web Version</title>
  <style>
    body { margin: 0; overflow: hidden; background: black; }
    #hud {
      position: absolute;
      top: 10px;
      left: 10px;
      color: white;
      font-family: Arial;
      font-size: 20px;
    }
  </style>
</head>
<body>

<div id="hud">HP: 100</div>

<script src="https://cdn.jsdelivr.net/npm/three@0.158.0/build/three.min.js"></script>

<script>
let scene = new THREE.Scene();
let camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
let renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// LUCI
const light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(10,20,10);
scene.add(light);
scene.add(new THREE.AmbientLight(0x888888));

// TERRENO
const groundGeometry = new THREE.PlaneGeometry(200,200,50,50);
groundGeometry.rotateX(-Math.PI/2);

for(let i=0;i<groundGeometry.attributes.position.count;i++){
  let y = Math.sin(i*0.3)*2;
  groundGeometry.attributes.position.setY(i,y);
}

groundGeometry.computeVertexNormals();

const groundMaterial = new THREE.MeshStandardMaterial({color:0x3e7f3e});
const ground = new THREE.Mesh(groundGeometry, groundMaterial);
scene.add(ground);

// ===== PANZER III PROCEDURALE =====
let tank = new THREE.Group();
scene.add(tank);

// Corpo
let body = new THREE.Mesh(
  new THREE.BoxGeometry(3,1,5),
  new THREE.MeshStandardMaterial({color:0x777777})
);
tank.add(body);

// Torretta
let turret = new THREE.Mesh(
  new THREE.BoxGeometry(2,0.8,2),
  new THREE.MeshStandardMaterial({color:0x555555})
);
turret.position.y = 1;
tank.add(turret);

// Cannone
let barrel = new THREE.Mesh(
  new THREE.BoxGeometry(0.3,0.3,4),
  new THREE.MeshStandardMaterial({color:0x444444})
);
barrel.position.z = 3;
turret.add(barrel);

tank.position.y = 2;

camera.position.set(0,15,-25);
camera.lookAt(tank.position);

// MOVIMENTO
let keys = {};
document.addEventListener("keydown", e => keys[e.key] = true);
document.addEventListener("keyup", e => keys[e.key] = false);

// PROIETTILI
let bullets = [];

function shoot(){
  let bullet = new THREE.Mesh(
    new THREE.SphereGeometry(0.3),
    new THREE.MeshBasicMaterial({color:0x000000})
  );
  
  bullet.position.copy(barrel.getWorldPosition(new THREE.Vector3()));
  
  let direction = new THREE.Vector3(0,0,1);
  direction.applyQuaternion(turret.quaternion);
  
  bullet.velocity = direction.multiplyScalar(0.8);
  
  scene.add(bullet);
  bullets.push(bullet);
}

document.addEventListener("click", shoot);

// LOOP
function animate(){
  requestAnimationFrame(animate);

  if(keys["w"]) tank.translateZ(0.5);
  if(keys["s"]) tank.translateZ(-0.5);
  if(keys["a"]) tank.rotation.y += 0.03;
  if(keys["d"]) tank.rotation.y -= 0.03;

  bullets.forEach(b=>{
    b.position.add(b.velocity);
  });

  camera.position.x = tank.position.x;
  camera.position.z = tank.position.z - 25;
  camera.lookAt(tank.position);

  renderer.render(scene,camera);
}

animate();
</script>
</body>
</html>
