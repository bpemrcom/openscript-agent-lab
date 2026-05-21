async function loadTree() {
  const response = await fetch("/api/project-tree", { headers: { Accept: "application/json" } });
  if (!response.ok) {
    throw new Error("Не удалось загрузить дерево проекта");
  }
  return response.json();
}

function createNode(node) {
  const li = document.createElement("li");
  const wrapper = document.createElement("div");
  const isFolder = node.type === "dir";

  wrapper.className = `node ${isFolder ? "node--folder" : "node--file"}`;

  const icon = document.createElement("span");
  icon.className = "node__icon";
  icon.textContent = isFolder ? "▸" : "•";

  const label = document.createElement("span");
  label.textContent = node.name;

  wrapper.append(icon, label);
  li.appendChild(wrapper);

  if (isFolder) {
    const childrenContainer = document.createElement("ul");
    childrenContainer.className = "children";
    childrenContainer.hidden = true;

    const children = Array.isArray(node.children) ? node.children : [];
    for (const child of children) {
      childrenContainer.appendChild(createNode(child));
    }

    wrapper.setAttribute("role", "button");
    wrapper.setAttribute("tabindex", "0");
    wrapper.setAttribute("aria-expanded", "false");

    const toggle = () => {
      const willOpen = childrenContainer.hidden;
      childrenContainer.hidden = !willOpen;
      wrapper.setAttribute("aria-expanded", String(willOpen));
      icon.textContent = willOpen ? "▾" : "▸";
    };

    wrapper.addEventListener("click", toggle);
    wrapper.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        toggle();
      }
    });

    li.appendChild(childrenContainer);
  }

  return li;
}

async function init() {
  const mount = document.getElementById("tree");
  try {
    const tree = await loadTree();
    const rootList = document.createElement("ul");
    rootList.appendChild(createNode(tree));
    mount.replaceChildren(rootList);
  } catch (error) {
    mount.textContent = "Не удалось загрузить структуру проекта.";
    console.error(error);
  }
}

init();
