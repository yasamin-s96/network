
const Container = ({ children }) => {
    return (
        <div className="h-screen w-screen flex items-center justify-center bg-img bg-cover bg-center bg-no-repeat">
            {children}
        </div>
    )
}

export default Container